#!/usr/bin/env python3
"""Build video/nca-aiio-overview.mp4 (silent explainer, 1920x1080, 30 fps).

Needs Pillow and ffmpeg:  python make_video.py
"""
import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
OUT = Path(__file__).parent
TMP = OUT / "_build"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BG, FG, MUTED, GREEN, BOX = (16, 20, 24), (240, 240, 240), (160, 170, 180), (118, 185, 0), (34, 42, 50)


def f(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def base(title, step):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    d.text((100, 70), title, font=f(64, True), fill=FG)
    d.text((W - 360, H - 70), f"NCA-AIIO  ·  {step}", font=f(28), fill=MUTED)
    return im, d


def bullets(d, items, y=220, size=40, gap=78):
    for it in items:
        d.ellipse([110, y + 14, 126, y + 30], fill=GREEN)
        d.text((150, y), it, font=f(size), fill=FG)
        y += gap


def box(d, xy, text, color=BOX, size=34, outline=GREEN):
    d.rounded_rectangle(xy, 18, fill=color, outline=outline, width=3)
    x0, y0, x1, y1 = xy
    lines = text.split("\n")
    lh = size + 10
    ty = (y0 + y1) / 2 - lh * len(lines) / 2
    for ln in lines:
        tw = d.textlength(ln, font=f(size, True))
        d.text(((x0 + x1) / 2 - tw / 2, ty), ln, font=f(size, True), fill=FG)
        ty += lh


def arrow(d, x0, y0, x1, y1):
    d.line([x0, y0, x1, y1], fill=GREEN, width=6)
    d.polygon([(x1, y1), (x1 - 22, y1 - 14), (x1 - 22, y1 + 14)], fill=GREEN)


def slides():
    s = []
    # 1 title
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    d.text((140, 330), "NVIDIA-Certified Associate", font=f(56), fill=MUTED)
    d.text((140, 410), "AI Infrastructure & Operations", font=f(96, True), fill=FG)
    d.text((140, 540), "NCA-AIIO — the 3-minute map of the exam", font=f(48), fill=GREEN)
    d.text((140, 680), "50 questions  ·  60 minutes  ·  online  ·  US $125  ·  valid 2 years", font=f(40), fill=FG)
    s.append((im, 10))

    # 2 domains bar
    im, d = base("Three domains. Study by weight.", "1/12")
    for i, (name, pct, n) in enumerate([("1  Essential AI Knowledge", 38, 19), ("2  AI Infrastructure", 40, 20), ("3  AI Operations", 22, 11)]):
        y = 260 + i * 210
        d.text((110, y), name, font=f(44, True), fill=FG)
        d.rectangle([110, y + 70, 110 + pct * 38, y + 140], fill=GREEN)
        d.text((130 + pct * 38, y + 78), f"{pct}%  ≈ {n} questions", font=f(44), fill=FG)
    s.append((im, 14))

    # 3 software stack
    im, d = base("Domain 1 · The NVIDIA software stack", "2/12")
    layers = [("Apps & frameworks: NeMo · PyTorch · RAPIDS · Riva · Merlin · Clara", (40, 60, 70)),
              ("Deploy: TensorRT (optimize) → Triton / NIM (serve)", (40, 70, 55)),
              ("CUDA-X libraries: cuDNN · cuBLAS · NCCL · DALI", (45, 55, 75)),
              ("CUDA  +  GPU driver  +  Container Toolkit", (60, 50, 45)),
              ("GPU hardware: Blackwell · Hopper · Ada · Ampere", (30, 30, 30))]
    for i, (t, c) in enumerate(layers):
        box(d, [160, 200 + i * 150, 1760, 320 + i * 150], t, color=c, size=38)
    s.append((im, 16))

    # 4 training vs inference
    im, d = base("Domain 1 · Training vs inference", "3/12")
    box(d, [120, 220, 900, 900], "TRAINING\n\nforward + backward\nupdates weights\n~16 bytes / param\nBF16 · FP8\nmany GPUs, east-west\nInfiniBand + NCCL\nmetric: time-to-train", size=40)
    box(d, [1020, 220, 1800, 900], "INFERENCE\n\nforward only\nweights fixed\n~2 bytes / param (FP16)\nFP8 · INT8 · FP4\nscale out replicas\nTensorRT + Triton/NIM\nmetric: latency", size=40)
    s.append((im, 16))

    # 5 GPU vs CPU
    im, d = base("Domain 1 · GPU vs CPU", "4/12")
    bullets(d, ["CPU: few powerful cores → low latency, serial logic",
                "GPU: thousands of cores in SMs → high throughput",
                "Tensor Cores do the matrix math of AI",
                "Warp = 32 threads · HBM memory = TB/s bandwidth",
                "Ampere: MIG, TF32  ·  Hopper: FP8  ·  Blackwell: FP4",
                "DGX = full NVIDIA system  ·  HGX = board for OEM servers"])
    s.append((im, 16))

    # 6 cluster networks
    im, d = base("Domain 2 · A cluster has four networks", "5/12")
    box(d, [760, 460, 1160, 640], "DGX node\n8 GPUs", size=44)
    for (x0, y0, x1, y1, t), (ax0, ay0, ax1, ay1) in [
        ((120, 200, 620, 360, "Compute fabric\nIB NDR 400 Gb/s / GPU"), (760, 520, 620, 300)),
        ((1300, 200, 1800, 360, "Storage fabric\nparallel file system"), (1160, 520, 1300, 300)),
        ((120, 760, 620, 920, "In-band mgmt\nSSH, jobs, updates"), (760, 600, 620, 820)),
        ((1300, 760, 1800, 920, "Out-of-band mgmt\nBMC · IPMI · Redfish"), (1160, 600, 1300, 820))]:
        box(d, [x0, y0, x1, y1], t, size=32)
        d.line([ax0, ay0, ax1, ay1], fill=GREEN, width=6)
    s.append((im, 16))

    # 7 networking
    im, d = base("Domain 2 · Networking for AI", "6/12")
    bullets(d, ["Inside node: NVLink + NVSwitch (900 GB/s H100, 1.8 TB/s B200)",
                "Between nodes: InfiniBand — RDMA, lossless credits, Subnet Manager",
                "Or Ethernet: RoCE v2 + PFC + ECN  →  Spectrum-X",
                "GPUDirect RDMA: NIC ↔ GPU memory, no CPU copy",
                "Non-blocking 1:1, rail-optimized fat-tree, 1 NIC per GPU",
                "Gb/s ÷ 8 = GB/s   (400 Gb/s = 50 GB/s)"], size=38)
    s.append((im, 18))

    # 8 power & cooling
    im, d = base("Domain 2 · Power, cooling, facility", "7/12")
    bullets(d, ["DGX H100 ≈ 10.2 kW · DGX B200 ≈ 14.3 kW",
                "4 × DGX H100 per rack ≈ 41 kW",
                "Air limit ≈ 30–40 kW/rack → then liquid cooling (CDU)",
                "GB200 NVL72: 72 GPUs, liquid-cooled rack",
                "PUE = facility ÷ IT power  (lower is better, 1.0 ideal)",
                "1 W = 3.412 BTU/hr  ·  2N = two full power paths"])
    s.append((im, 16))

    # 9 DPU, cloud, scaling
    im, d = base("Domain 2 · DPU, scale, on-prem vs cloud", "8/12")
    bullets(d, ["BlueField DPU: offload network, storage, security · DOCA SDK",
                "DPU = separate trust domain → zero-trust isolation",
                "SuperPOD: scalable units of 32 DGX nodes",
                "Scale up = NVLink domain · Scale out = more nodes",
                "Cloud: OpEx, bursty, fast start · egress fees",
                "On-prem: CapEx, steady use, data sovereignty"], size=38)
    s.append((im, 16))

    # 10 monitoring
    im, d = base("Domain 3 · Monitor GPUs", "9/12")
    for i, t in enumerate(["GPUs", "DCGM\nExporter :9400", "Prometheus", "Grafana\n+ alerts"]):
        box(d, [120 + i * 450, 210, 470 + i * 450, 370], t, size=36)
        if i:
            arrow(d, 470 + (i - 1) * 450, 290, 120 + i * 450, 290)
    bullets(d, ["SM_ACTIVE is better than GPU_UTIL · hot + low clock = thermal throttle",
                "ECC: single-bit corrected, double-bit (XID 48) not corrected",
                "XID 74 NVLink · XID 79 fell off the bus → drain node",
                "dcgmi diag -r 1 / 2 / 3  ·  BMC power-cycles frozen nodes"], y=470, size=38)
    s.append((im, 18))

    # 11 orchestration + virtualization
    im, d = base("Domain 3 · Schedule and share GPUs", "10/12")
    bullets(d, ["Slurm: sbatch · squeue · sinfo · drain · fair-share · backfill",
                "Kubernetes: GPU Operator → nvidia.com/gpu (device plugin)",
                "Run:ai: quotas and fractional GPUs · Base Command Manager: provisioning",
                "Time-slicing: shares, but NO memory isolation",
                "MIG: up to 7 hardware-isolated instances (e.g. 3g.40gb)",
                "vGPU: VMs on a hypervisor + license"], size=38)
    s.append((im, 18))

    # 12 how to study
    im, d = base("How to pass", "11/12")
    bullets(d, ["Week 1: Domain 1 notes + labs 01, 03",
                "Week 2: Domain 2 notes + labs 04, 09",
                "Week 3: Domain 3 notes + labs 02, 05–08, 10",
                "Week 4: 3 mock exams · python practice/quiz.py --exam 1",
                "Book the exam at 80%+ on every mock"])
    s.append((im, 14))

    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    d.text((140, 420), "Start with STUDY-PLAN.md", font=f(80, True), fill=FG)
    d.text((140, 540), "github.com/gvarun17/nca-aiio", font=f(52), fill=GREEN)
    s.append((im, 8))
    return s


def main():
    TMP.mkdir(exist_ok=True)
    parts = []
    for i, (im, dur) in enumerate(slides()):
        png = TMP / f"s{i:02d}.png"
        im.save(png)
        tmp, final = TMP / f"s{i:02d}.part.mp4", TMP / f"s{i:02d}.mp4"
        vf = f"format=yuv420p,loop=-1:1,trim=duration={dur},fade=t=in:st=0:d=0.5,fade=t=out:st={dur-0.5}:d=0.5"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(png), "-vf", vf,
                        "-r", "30", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                        str(tmp)], check=True)
        os.replace(tmp, final)
        parts.append(final)
    lst = TMP / "list.txt"
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    out = OUT / "nca-aiio-overview.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", "-movflags", "+faststart", str(out)], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
