#!/usr/bin/env python3
"""Lab 01 — CPU vs GPU matrix-multiply benchmark.

Runs on any machine. Uses the GPU only if PyTorch with CUDA is available
(for example a free Google Colab T4 runtime).

Usage:
    python benchmark.py                 # default sizes
    python benchmark.py --sizes 1024 4096 8192
"""
import argparse
import time

import numpy as np


def tflops(n: int, seconds: float) -> float:
    # One n x n matmul = 2 * n^3 floating point operations.
    return 2 * n**3 / seconds / 1e12


def bench_cpu(n: int, repeats: int = 3) -> float:
    a = np.random.rand(n, n).astype(np.float32)
    b = np.random.rand(n, n).astype(np.float32)
    a @ b  # warm-up
    t0 = time.perf_counter()
    for _ in range(repeats):
        a @ b
    return (time.perf_counter() - t0) / repeats


def bench_gpu(n: int, dtype_name: str, repeats: int = 10):
    import torch

    dtype = {"fp32": torch.float32, "fp16": torch.float16, "bf16": torch.bfloat16}[dtype_name]
    a = torch.rand(n, n, device="cuda", dtype=dtype)
    b = torch.rand(n, n, device="cuda", dtype=dtype)
    a @ b
    torch.cuda.synchronize()  # GPU calls are asynchronous; wait before timing
    t0 = time.perf_counter()
    for _ in range(repeats):
        a @ b
    torch.cuda.synchronize()
    return (time.perf_counter() - t0) / repeats


def gpu_available() -> bool:
    try:
        import torch

        return torch.cuda.is_available()
    except ImportError:
        return False


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--sizes", type=int, nargs="+", default=[512, 1024, 2048, 4096])
    args = p.parse_args()

    has_gpu = gpu_available()
    if has_gpu:
        import torch

        print(f"GPU found: {torch.cuda.get_device_name(0)}")
    else:
        print("No CUDA GPU found. CPU results only. (Run on Colab with a T4 GPU for the full lab.)")

    header = f"{'N':>6} | {'CPU fp32 ms':>11} | {'CPU TFLOPS':>10}"
    if has_gpu:
        header += f" | {'GPU fp32 ms':>11} | {'GPU fp16 ms':>11} | {'GPU fp16 TFLOPS':>15} | {'speedup fp16':>12}"
    print(header)
    print("-" * len(header))

    for n in args.sizes:
        c = bench_cpu(n)
        row = f"{n:>6} | {c*1e3:>11.2f} | {tflops(n, c):>10.3f}"
        if has_gpu:
            g32 = bench_gpu(n, "fp32")
            g16 = bench_gpu(n, "fp16")
            row += f" | {g32*1e3:>11.2f} | {g16*1e3:>11.2f} | {tflops(n, g16):>15.2f} | {c/g16:>11.0f}x"
        print(row)

    print("\nWhat to observe:")
    print(" 1. Bigger matrices give the GPU more parallel work, so the speedup grows.")
    print(" 2. FP16 is faster than FP32 on the GPU because Tensor Cores run FP16/BF16 math.")
    print(" 3. For tiny matrices, launch and transfer overhead hides the GPU advantage.")


if __name__ == "__main__":
    main()
