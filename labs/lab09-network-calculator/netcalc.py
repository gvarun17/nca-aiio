#!/usr/bin/env python3
"""Lab 09 — AI network calculator.

    python netcalc.py convert --gbps 400
    python netcalc.py allreduce --size-gb 14 --gpus 64 --link-gbps 400
    python netcalc.py fabric --nodes 128 --gpus-per-node 8 --switch-ports 64
    python netcalc.py oversub --down 32 --up 16
"""
import argparse
import math


def convert(a):
    print(f"{a.gbps:g} Gb/s = {a.gbps/8:g} GB/s  (divide bits by 8)")
    print(f"Per node with 8 such NICs: {a.gbps*8/1000:g} Tb/s = {a.gbps:g} GB/s")


def allreduce(a):
    n = a.gpus
    size_bytes = a.size_gb * 1e9
    bw_bytes = a.link_gbps / 8 * 1e9
    # Ring all-reduce: each GPU sends and receives 2*(N-1)/N of the data.
    traffic = 2 * (n - 1) / n * size_bytes
    t = traffic / bw_bytes
    print(f"Ring all-reduce of {a.size_gb:g} GB gradients across {n} GPUs at {a.link_gbps:g} Gb/s per GPU:")
    print(f"  data sent per GPU = 2(N-1)/N x size = {traffic/1e9:.2f} GB")
    print(f"  ideal time        = {t:.3f} s per step (bandwidth only, no latency/overlap)")
    nv = 900e9  # H100 NVLink GB/s per GPU (bidirectional total) — used as a rough intra-node comparison
    print(f"  same data on NVLink 900 GB/s ≈ {traffic/(nv/2):.3f} s  -> why tensor parallel stays inside the node")
    print("  Note: the slowest link sets the pace for ALL GPUs (synchronous training).")


def fabric(a):
    rails = a.gpus_per_node
    down = a.switch_ports // 2  # non-blocking: half the ports down, half up
    leaves_per_rail = math.ceil(a.nodes / down)
    leaves = rails * leaves_per_rail
    uplinks = leaves * down
    spines = math.ceil(uplinks / a.switch_ports)
    print(f"Rail-optimized, non-blocking 2-tier fat-tree for {a.nodes} nodes x {rails} GPUs ({a.nodes*rails} GPUs)")
    print(f"  switch radix         = {a.switch_ports} ports (e.g., Quantum-2 QM9700: 64 x NDR 400 Gb/s)")
    print(f"  rails                = {rails} (NIC n of every node -> rail n leaves)")
    print(f"  leaf switches        = {leaves}  ({leaves_per_rail} per rail, {down} down + {down} up ports each)")
    print(f"  spine switches       = {spines}")
    print(f"  node-to-leaf cables  = {a.nodes*rails}")
    print(f"  leaf-to-spine cables = {uplinks}")
    if leaves > a.switch_ports:
        print("  WARNING: more leaves than spine ports -> add a core tier (3-tier fat-tree).")


def oversub(a):
    r = a.down / a.up
    print(f"Oversubscription = downlink {a.down} / uplink {a.up} = {r:g}:1")
    print("  1:1 = non-blocking (required for the GPU compute fabric).")
    print("  >1:1 is acceptable for management or user networks, not for training all-reduce.")


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("convert"); c.add_argument("--gbps", type=float, required=True); c.set_defaults(f=convert)
    r = sp.add_parser("allreduce")
    r.add_argument("--size-gb", type=float, required=True)
    r.add_argument("--gpus", type=int, required=True)
    r.add_argument("--link-gbps", type=float, default=400)
    r.set_defaults(f=allreduce)
    f = sp.add_parser("fabric")
    f.add_argument("--nodes", type=int, required=True)
    f.add_argument("--gpus-per-node", type=int, default=8)
    f.add_argument("--switch-ports", type=int, default=64)
    f.set_defaults(f=fabric)
    o = sp.add_parser("oversub"); o.add_argument("--down", type=float, required=True); o.add_argument("--up", type=float, required=True); o.set_defaults(f=oversub)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
