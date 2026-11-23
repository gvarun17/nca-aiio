#!/usr/bin/env python3
"""Fake DCGM Exporter for practice on a machine with NO GPU.

Serves Prometheus metrics at http://localhost:9400/metrics with the same
metric names as the real NVIDIA DCGM Exporter. It simulates 8 GPUs:
  - GPU 2 runs hot and throttles (thermal problem)
  - GPU 5 is idle (low utilization)
  - GPU 6 has a rising single-bit ECC count and one XID 48 event after ~2 minutes

Usage:
    python fake_dcgm_exporter.py            # then open http://localhost:9400/metrics
"""
import math
import random
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

START = time.time()
HOST = "dgx-sim01"
MODEL = "NVIDIA H100 80GB HBM3"


def gpu_values(i: int, t: float) -> dict:
    wave = (math.sin(t / 30) + 1) / 2
    util = 92 + 6 * wave + random.uniform(-2, 2)
    temp = 62 + 6 * wave
    clock = 1980
    power = 560 + 100 * wave
    fb_used = 70000 + random.randint(-500, 500)
    sm_active = 0.78 + 0.1 * wave
    tensor = 0.55 + 0.1 * wave
    sbe = 0
    xid = 0
    if i == 2:  # thermal throttling
        temp = 86 + 3 * wave
        clock = 1350 + random.randint(-40, 40)
    if i == 5:  # idle / data starvation
        util = 8 + random.uniform(-3, 3)
        sm_active = 0.05
        tensor = 0.01
        power = 140
        temp = 40
    if i == 6:  # memory going bad
        sbe = int(t // 20)
        if t > 120:
            xid = 48
    return {
        "DCGM_FI_DEV_GPU_UTIL": round(max(util, 0)),
        "DCGM_FI_DEV_FB_USED": fb_used,
        "DCGM_FI_DEV_FB_FREE": 81559 - fb_used,
        "DCGM_FI_DEV_GPU_TEMP": round(temp),
        "DCGM_FI_DEV_POWER_USAGE": round(power, 1),
        "DCGM_FI_DEV_SM_CLOCK": clock,
        "DCGM_FI_DEV_ECC_SBE_VOL_TOTAL": sbe,
        "DCGM_FI_DEV_ECC_DBE_VOL_TOTAL": 1 if xid == 48 else 0,
        "DCGM_FI_DEV_XID_ERRORS": xid,
        "DCGM_FI_PROF_SM_ACTIVE": round(sm_active, 3),
        "DCGM_FI_PROF_PIPE_TENSOR_ACTIVE": round(tensor, 3),
    }


def render() -> str:
    t = time.time() - START
    lines = []
    for metric in gpu_values(0, t):
        lines.append(f"# HELP {metric} Simulated DCGM field.")
        lines.append(f"# TYPE {metric} gauge")
        for i in range(8):
            v = gpu_values(i, t)[metric]
            labels = f'gpu="{i}",UUID="GPU-sim-{i:04d}",device="nvidia{i}",modelName="{MODEL}",Hostname="{HOST}"'
            lines.append(f"{metric}{{{labels}}} {v}")
    return "\n".join(lines) + "\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_response(404)
            self.end_headers()
            return
        body = render().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print("Fake DCGM Exporter on http://0.0.0.0:9400/metrics  (Ctrl+C to stop)")
    HTTPServer(("0.0.0.0", 9400), Handler).serve_forever()
