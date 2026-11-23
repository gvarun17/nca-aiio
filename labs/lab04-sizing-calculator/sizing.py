#!/usr/bin/env python3
"""Lab 04 — AI infrastructure sizing calculator.

Estimates GPU memory, GPU count, nodes, racks, power, cooling, and PUE.
Numbers are rules of thumb for exam-level reasoning, not a vendor quote.

Examples:
    python sizing.py memory --params 70 --mode train
    python sizing.py memory --params 70 --mode infer --precision fp8
    python sizing.py cluster --gpus 256 --system dgx-h100 --rack-kw 40
    python sizing.py pue --facility-kw 1300 --it-kw 1000
    python sizing.py cooling --kw 41
"""
import argparse
import math

BYTES_PER_PARAM = {"fp32": 4, "bf16": 2, "fp16": 2, "fp8": 1, "int8": 1, "fp4": 0.5, "int4": 0.5}

SYSTEMS = {
    #             gpus, GB per GPU, max kW, rack units
    "dgx-h100": (8, 80, 10.2, 8),
    "dgx-h200": (8, 141, 10.2, 8),
    "dgx-b200": (8, 180, 14.3, 10),
    "dgx-a100": (8, 80, 6.5, 6),
}


def cmd_memory(a):
    p = a.params * 1e9
    if a.mode == "train":
        # Mixed precision + Adam: weights bf16 (2) + grads (2) + fp32 master weights (4) + Adam m,v (8) = 16 B/param
        per_param = 16
        base = p * per_param
        act = base * a.activation_overhead
        total = base + act
        print(f"Training {a.params:g}B params (mixed precision + Adam):")
        print(f"  weights+grads+optimizer = {base/1e9:,.0f} GB (16 bytes/param)")
        print(f"  activations (~{a.activation_overhead:.0%} rule of thumb) = {act/1e9:,.0f} GB")
    else:
        per_param = BYTES_PER_PARAM[a.precision]
        base = p * per_param
        kv = base * a.kv_overhead
        total = base + kv
        print(f"Inference {a.params:g}B params at {a.precision} ({per_param} bytes/param):")
        print(f"  weights = {base/1e9:,.0f} GB")
        print(f"  KV cache + runtime (~{a.kv_overhead:.0%} rule of thumb) = {kv/1e9:,.0f} GB")
    print(f"  TOTAL ≈ {total/1e9:,.0f} GB")
    for gpu, gb in (("L4 24GB", 24), ("L40S 48GB", 48), ("H100 80GB", 80), ("H200 141GB", 141), ("B200 180GB", 180)):
        n = math.ceil(total / (gb * 1e9))
        print(f"  minimum {gpu:<11}: {n:>4} GPU(s)  (memory only; compute time not included)")


def cmd_cluster(a):
    gpus_per, gb, kw, ru = SYSTEMS[a.system]
    nodes = math.ceil(a.gpus / gpus_per)
    total_kw = nodes * kw
    per_rack = max(1, min(int(a.rack_kw // kw), a.rack_units // ru))
    racks = math.ceil(nodes / per_rack)
    sus = nodes / 32
    print(f"{a.gpus} GPUs on {a.system}:")
    print(f"  nodes               = {nodes}  ({sus:.2f} SuperPOD scalable units of 32 nodes)")
    print(f"  total GPU memory    = {nodes*gpus_per*gb/1000:,.1f} TB")
    print(f"  IT power (max)      = {total_kw:,.1f} kW")
    print(f"  systems per rack    = {per_rack}  (rack limit {a.rack_kw} kW, {a.rack_units} U usable)")
    print(f"  compute racks       = {racks}")
    print(f"  compute NICs        = {nodes*gpus_per} x 400 Gb/s (1 NIC per GPU, rail-optimized)")
    print(f"  heat to remove      = {total_kw*3412:,.0f} BTU/hr = {total_kw/3.517:,.1f} tons of cooling")
    print(f"  facility power at PUE {a.pue} = {total_kw*a.pue:,.1f} kW")


def cmd_pue(a):
    pue = a.facility_kw / a.it_kw
    print(f"PUE  = {a.facility_kw} / {a.it_kw} = {pue:.2f}")
    print(f"DCiE = {1/pue:.0%} of facility power reaches IT equipment")
    print(f"Overhead (cooling, power losses, lighting) = {a.facility_kw - a.it_kw:,.0f} kW")


def cmd_cooling(a):
    print(f"{a.kw} kW of IT load = {a.kw*3412:,.0f} BTU/hr = {a.kw/3.517:.1f} tons of cooling")
    if a.kw <= 15:
        print("Traditional air cooling is usually fine.")
    elif a.kw <= 40:
        print("High density: hot/cold aisle containment, maybe rear-door heat exchangers.")
    else:
        print("Very high density: plan direct liquid cooling (CDU + facility water).")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    m = sp.add_parser("memory")
    m.add_argument("--params", type=float, required=True, help="model size in billions of parameters")
    m.add_argument("--mode", choices=["train", "infer"], default="infer")
    m.add_argument("--precision", choices=list(BYTES_PER_PARAM), default="fp16")
    m.add_argument("--activation-overhead", type=float, default=0.25)
    m.add_argument("--kv-overhead", type=float, default=0.20)
    m.set_defaults(func=cmd_memory)

    c = sp.add_parser("cluster")
    c.add_argument("--gpus", type=int, required=True)
    c.add_argument("--system", choices=list(SYSTEMS), default="dgx-h100")
    c.add_argument("--rack-kw", type=float, default=40)
    c.add_argument("--rack-units", type=int, default=42)
    c.add_argument("--pue", type=float, default=1.3)
    c.set_defaults(func=cmd_cluster)

    u = sp.add_parser("pue")
    u.add_argument("--facility-kw", type=float, required=True)
    u.add_argument("--it-kw", type=float, required=True)
    u.set_defaults(func=cmd_pue)

    k = sp.add_parser("cooling")
    k.add_argument("--kw", type=float, required=True)
    k.set_defaults(func=cmd_cooling)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
