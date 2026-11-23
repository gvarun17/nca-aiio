# NCA-AIIO Cheat Sheet

## Numbers

| Item | Value |
|---|---|
| Exam | 50 Q, 60 min, $125, 2-year validity |
| Domains | 38% Essential AI · 40% Infrastructure · 22% Operations |
| H100 SXM | 80 GB HBM3, ~3.35 TB/s, NVLink 4 = 900 GB/s, up to 700 W |
| H200 | 141 GB HBM3e, ~4.8 TB/s |
| B200 | up to 192 GB HBM3e (180 GB in DGX B200), ~8 TB/s, NVLink 5 = 1.8 TB/s |
| DGX H100 | 8 GPUs, 640 GB, 4 NVSwitch, 8x CX-7 400 Gb/s, 2 TB RAM, ~10.2 kW, 8U |
| DGX B200 | 8 GPUs, 1,440 GB, 2 NVSwitch, 14.4 TB/s NVLink total, ~14.3 kW, 10U |
| DGX A100 | 8 GPUs, ~6.5 kW |
| GB200 NVL72 | 72 GPUs + 36 Grace CPUs, one NVLink domain, liquid-cooled, ~120+ kW rack |
| SuperPOD SU | 32 DGX nodes = 256 GPUs; 4 SU ≈ 127 nodes + UFM |
| L4 | 72 W, inference/video · L40S: 48 GB, inference/graphics/fine-tune |
| MIG | up to 7 instances (A100, H100, H200, B200) |
| Warp | 32 threads |
| IB speeds | EDR 100 · HDR 200 · NDR 400 · XDR 800 Gb/s |
| Bits → bytes | ÷ 8 (400 Gb/s = 50 GB/s) |
| PCIe Gen5 x16 | ~64 GB/s per direction |
| NVLink-C2C | 900 GB/s (Grace ↔ GPU) |
| PUE | facility ÷ IT (1.0 ideal; lower = better) |
| Heat | 1 W = 3.412 BTU/hr; 1 ton = 12,000 BTU/hr ≈ 3.52 kW |
| Air cooling limit | ~30–40 kW per rack (with containment) |
| Memory per param | FP32 4 B · FP16/BF16 2 B · FP8/INT8 1 B · FP4 0.5 B · training ≈ 16 B |
| DCGM Exporter port | 9400 · Triton: 8000 HTTP, 8001 gRPC, 8002 metrics |

## Architectures

| Arch | Firsts |
|---|---|
| Ampere (A100) | MIG, TF32, NVLink 3 (600 GB/s) |
| Hopper (H100/H200) | Transformer Engine, FP8, NVLink 4 (900 GB/s), confidential computing |
| Ada (L40S/L4) | FP8 inference + graphics, low power |
| Blackwell (B200/GB200) | FP4, 2nd-gen Transformer Engine, NVLink 5 (1.8 TB/s) |

## Need → product

| Need | Product |
|---|---|
| Optimize inference | TensorRT / TensorRT-LLM |
| Serve models | Triton (Dynamo), NIM |
| Multi-GPU comms | NCCL |
| Data loading on GPU | DALI |
| Data science / ETL on GPU | RAPIDS |
| Build LLMs | NeMo |
| Containers, models | NGC |
| Supported enterprise suite | NVIDIA AI Enterprise |
| GPU monitoring | DCGM |
| GPUs on Kubernetes | GPU Operator; Network Operator for RDMA |
| GPU quotas/fractions | Run:ai |
| Cluster provisioning | Base Command Manager; Mission Control |
| IB fabric mgmt | UFM / Subnet Manager |
| DPU programming | DOCA |
| Recommenders | Merlin · Speech: Riva · Video: Metropolis · Health: Clara · Security: Morpheus · Robots: Isaac · Digital twins: Omniverse · Cars: DRIVE · Video calls: Maxine |
| Edge device | Jetson · Industrial edge: IGX · Edge fleet mgmt: Fleet Command |
| OEM 8-GPU board | HGX · Complete NVIDIA system: DGX |

## Networking

- **4 networks:** compute (east-west GPU), storage, in-band mgmt, out-of-band (BMC).
- **InfiniBand:** native RDMA, credit-based lossless, Subnet Manager assigns LIDs, SHARP in-network reduction, adaptive routing.
- **RoCE v2:** RDMA over UDP/IP (routable); needs **PFC + ECN (DCQCN)**.
- **Spectrum-X:** Spectrum-4 switch + BlueField-3 SuperNIC = AI Ethernet.
- **GPUDirect RDMA:** NIC ↔ GPU memory. **GPUDirect Storage:** storage ↔ GPU memory.
- Training fabric: **non-blocking 1:1, rail-optimized fat-tree**, 1 NIC per GPU.

## Operations

- **BMC** (IPMI old, **Redfish** REST) on OOB network: power, console, sensors, firmware.
- **nvidia-smi:** one node. `-q`, `topo -m`, `dmon`, `--query-gpu`, `mig -lgip`.
- **DCGM:** `dcgmi diag -r 1/2/3` (quick/medium/long), `dcgmi health`.
- **XID:** 13/31 app · 48 DBE ECC · 63/64 row remap · 74 NVLink · **79 fell off bus** · 94/95 ECC contained/uncontained.
- GPU_UTIL = time busy; **SM_ACTIVE** = how much is busy.
- Hot + low clocks = **thermal throttle**. At power limit + low clocks = **power throttle**.
- **Slurm:** sbatch, srun, squeue, sinfo, scancel, scontrol (drain/resume), sacct; partitions, fair-share, backfill; Pyxis+Enroot for containers.
- **Kubernetes:** `nvidia.com/gpu`; GPU Operator = driver, toolkit, device plugin, GFD, DCGM exporter, MIG manager.
- **Sharing:** passthrough (1 VM) · time-slicing (no isolation) · MPS · **MIG (HW isolation, ≤7)** · vGPU (hypervisor + license).
