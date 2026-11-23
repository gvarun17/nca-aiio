#!/usr/bin/env python3
"""Lab 02 — Analyze nvidia-smi CSV output and kernel XID logs.

Works with the sample files in this folder, or with real data:

    nvidia-smi --query-gpu=timestamp,index,name,utilization.gpu,memory.used,memory.total,\
temperature.gpu,power.draw,power.limit,clocks.sm,clocks.max.sm,\
ecc.errors.uncorrected.volatile.total,ecc.errors.corrected.volatile.total \
--format=csv,noheader,nounits > my_metrics.csv
    sudo dmesg -T | grep -i xid > my_kernel.log

Usage:
    python analyze.py --metrics sample_gpu_metrics.csv --log sample_kernel.log
"""
import argparse
import csv
import re
from collections import defaultdict

XID_TABLE = {
    13: ("Graphics engine exception", "Usually an application bug. Check the code / CUDA version.", "LOW"),
    31: ("GPU memory page fault (MMU fault)", "Usually an application bug (illegal memory address).", "LOW"),
    43: ("GPU stopped processing", "App killed or hung. Check the application.", "LOW"),
    45: ("Preemptive cleanup", "Follows another error or app termination.", "LOW"),
    48: ("Double-bit ECC error (uncorrectable)", "Drain the node. Reset the GPU. Run dcgmi diag -r 3.", "HIGH"),
    63: ("Row remapping event", "Memory repair pending. Reset GPU at next maintenance.", "MEDIUM"),
    64: ("Row remapping failure", "Memory repair failed. Drain node and RMA the GPU.", "HIGH"),
    74: ("NVLink error", "Check NVLink/NVSwitch. Run diagnostics. Possible hardware fault.", "HIGH"),
    79: ("GPU has fallen off the bus", "Drain node. Power-cycle via BMC. Check PCIe/power/thermal. Likely RMA.", "CRITICAL"),
    92: ("High single-bit ECC error rate", "Monitor. Plan GPU replacement if it continues.", "MEDIUM"),
    94: ("Contained ECC error", "App affected. Restart app. GPU can continue.", "MEDIUM"),
    95: ("Uncontained ECC error", "Reset the GPU. Drain node until reset.", "HIGH"),
}

XID_RE = re.compile(r"^(\w+ +\d+ [\d:]+) (\S+) kernel: NVRM: Xid \(PCI:([0-9a-fA-F:.]+)\): (\d+),")


def analyze_metrics(path: str) -> None:
    print("=" * 70)
    print("GPU METRICS REPORT")
    print("=" * 70)
    fields = ["timestamp", "index", "name", "utilization.gpu", "memory.used", "memory.total",
              "temperature.gpu", "power.draw", "power.limit", "clocks.sm", "clocks.max.sm",
              "ecc.errors.uncorrected.volatile.total", "ecc.errors.corrected.volatile.total"]
    per_node = defaultdict(list)
    with open(path, newline="") as f:
        rows = [[c.strip() for c in r] for r in csv.reader(f) if r]
    if rows and rows[0][0].startswith("timestamp"):
        # Header present: remove unit suffixes such as " [%]".
        header = [re.sub(r"\s*\[.*\]$", "", h) for h in rows[0]]
        rows = rows[1:]
    else:
        header = fields  # real nvidia-smi output with "noheader"
    for r in rows:
        row = dict(zip(header, r))
        for k, v in row.items():  # strip units if "nounits" was not used
            row[k] = re.sub(r"\s*(MiB|W|MHz|%|C)$", "", v)
        for k in ("ecc.errors.uncorrected.volatile.total", "ecc.errors.corrected.volatile.total"):
            if not row.get(k, "0").isdigit():
                row[k] = "0"  # "[N/A]" when ECC is not supported (e.g., some consumer GPUs)
        per_node[row.get("node", "local")].append(row)

    for node, gpus in per_node.items():
        utils = [float(g["utilization.gpu"]) for g in gpus]
        print(f"\nNode {node}: {len(gpus)} GPUs, average util {sum(utils)/len(utils):.0f}%")
        for g in gpus:
            idx = g["index"]
            util = float(g["utilization.gpu"])
            used, total = float(g["memory.used"]), float(g["memory.total"])
            temp = float(g["temperature.gpu"])
            pwr, plim = float(g["power.draw"]), float(g["power.limit"])
            sm, smax = float(g["clocks.sm"]), float(g["clocks.max.sm"])
            dbe = int(g["ecc.errors.uncorrected.volatile.total"])
            sbe = int(g["ecc.errors.corrected.volatile.total"])
            findings = []
            if dbe > 0:
                findings.append(f"UNCORRECTED ECC={dbe} -> drain node, reset GPU, run dcgmi diag -r 3")
            if sbe > 0:
                findings.append(f"corrected ECC={sbe} -> watch the trend")
            if sm < 0.9 * smax and util > 50:
                if temp >= 85:
                    findings.append(f"THERMAL THROTTLE (temp {temp:.0f}C, SM {sm:.0f}/{smax:.0f} MHz) -> check airflow/cooling")
                elif pwr >= 0.97 * plim:
                    findings.append(f"POWER THROTTLE (power {pwr:.0f}/{plim:.0f} W) -> check power cap / workload")
                else:
                    findings.append("clocks below max -> run nvidia-smi -q -d PERFORMANCE for throttle reason")
            if util < 20 and used > 0:
                findings.append(f"LOW UTIL {util:.0f}% -> data pipeline, small batch, or idle job? consider MIG/sharing")
            if used / total > 0.97:
                findings.append(f"MEMORY {used/total:.0%} full -> OOM risk")
            if util == 0 and used == 0 and sm < 0.5 * smax:
                findings.append("GPU idle with no memory use and very low clocks -> check if GPU is healthy/visible")
            status = "OK" if not findings else "CHECK"
            print(f"  GPU{idx}: util {util:>3.0f}%  mem {used/total:>4.0%}  temp {temp:>3.0f}C  "
                  f"power {pwr:>5.0f}W  [{status}]")
            for fnd in findings:
                print(f"        - {fnd}")


def analyze_log(path: str) -> None:
    print("\n" + "=" * 70)
    print("XID ERROR REPORT")
    print("=" * 70)
    with open(path) as f:
        for line in f:
            m = XID_RE.search(line)
            if not m:
                continue
            ts, node, pci, xid = m.group(1), m.group(2), m.group(3), int(m.group(4))
            name, action, sev = XID_TABLE.get(xid, ("Unknown XID", "Check the NVIDIA XID documentation.", "?"))
            print(f"[{sev:<8}] {ts} {node} GPU@{pci} XID {xid}: {name}")
            print(f"           Action: {action}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--metrics", default="sample_gpu_metrics.csv")
    p.add_argument("--log", default="sample_kernel.log")
    a = p.parse_args()
    analyze_metrics(a.metrics)
    analyze_log(a.log)


if __name__ == "__main__":
    main()
