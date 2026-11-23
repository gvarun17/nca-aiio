#!/usr/bin/env python3
"""Lab 08 — MIG planner (simplified model).

Picks the smallest MIG profile for each workload and packs instances onto GPUs.
Model: a GPU has 7 compute slices and 8 memory slices; max 7 instances per GPU.
Real MIG placement has extra position rules — always confirm with
`nvidia-smi mig -lgipp` on the real GPU.

Usage:
    python mig_planner.py --gpu h100-80gb --workloads 8 8 12 30 35 70
    python mig_planner.py --gpu a100-40gb --workloads 4 4 4 9 18
    python mig_planner.py --gpu h100-80gb --list
"""
import argparse

# name: (compute slices, memory slices, memory GB)
PROFILES = {
    "h100-80gb": {"1g.10gb": (1, 1, 10), "1g.20gb": (1, 2, 20), "2g.20gb": (2, 2, 20),
                  "3g.40gb": (3, 4, 40), "4g.40gb": (4, 4, 40), "7g.80gb": (7, 8, 80)},
    "a100-40gb": {"1g.5gb": (1, 1, 5), "1g.10gb": (1, 2, 10), "2g.10gb": (2, 2, 10),
                  "3g.20gb": (3, 4, 20), "4g.20gb": (4, 4, 20), "7g.40gb": (7, 8, 40)},
    "a100-80gb": {"1g.10gb": (1, 1, 10), "1g.20gb": (1, 2, 20), "2g.20gb": (2, 2, 20),
                  "3g.40gb": (3, 4, 40), "4g.40gb": (4, 4, 40), "7g.80gb": (7, 8, 80)},
}


def pick(profiles, need_gb):
    # Smallest memory first, then fewest compute slices.
    fits = [(m, c, n) for n, (c, ms, m) in profiles.items() if m >= need_gb]
    if not fits:
        return None
    return sorted(fits)[0][2]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gpu", choices=list(PROFILES), default="h100-80gb")
    p.add_argument("--workloads", type=float, nargs="*", default=[], help="GPU memory need of each workload in GB")
    p.add_argument("--list", action="store_true")
    a = p.parse_args()
    profiles = PROFILES[a.gpu]

    if a.list or not a.workloads:
        print(f"MIG profiles for {a.gpu}:  <compute slices>g.<memory>gb")
        for n, (c, ms, m) in profiles.items():
            print(f"  {n:<8} compute {c}/7  memory slices {ms}/8  ({m} GB)  max per GPU: {min(7 // c, 8 // ms)}")
        if not a.workloads:
            return

    plan = []
    for i, need in enumerate(a.workloads):
        prof = pick(profiles, need)
        if prof is None:
            print(f"Workload {i} needs {need} GB: too big for one GPU -> use whole GPUs / multi-GPU, not MIG.")
            continue
        plan.append((i, need, prof))

    # First-fit decreasing on compute slices.
    gpus = []  # each: dict(c=used compute, m=used mem, items=[...])
    for i, need, prof in sorted(plan, key=lambda x: -profiles[x[2]][0]):
        c, ms, _ = profiles[prof]
        for g in gpus:
            if g["c"] + c <= 7 and g["m"] + ms <= 8 and len(g["items"]) < 7:
                g["c"] += c; g["m"] += ms; g["items"].append((i, need, prof))
                break
        else:
            gpus.append({"c": c, "m": ms, "items": [(i, need, prof)]})

    print(f"\nPlan on {a.gpu}: {len(gpus)} GPU(s) instead of {len(plan)} whole GPUs")
    for n, g in enumerate(gpus):
        items = ", ".join(f"w{i}({need:g}GB)->{prof}" for i, need, prof in g["items"])
        print(f"  GPU{n}: compute {g['c']}/7, memory {g['m']}/8 slices | {items}")
    print("\nEach MIG instance has dedicated SMs, L2 cache and memory: hardware isolation and predictable QoS.")


if __name__ == "__main__":
    main()
