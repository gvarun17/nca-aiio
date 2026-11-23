# Flashcards

Cover the right column. Say the answer. Then check. Mark cards you miss and repeat them the next day.

## Domain 1

| Front | Back |
|---|---|
| Inference optimizer | TensorRT |
| Inference server | Triton (Dynamo) |
| Packaged model microservice | NIM |
| Multi-GPU collectives | NCCL |
| GPU data loading | DALI |
| GPU pandas / scikit-learn | RAPIDS (cuDF / cuML) |
| LLM build/customize | NeMo |
| Container catalog | NGC |
| Must be on the host, not in container | GPU driver |
| Training memory per parameter (Adam, mixed) | ~16 bytes |
| FP16 inference memory per parameter | 2 bytes |
| Main inference metric | Latency (and throughput, cost per query) |
| Tensor parallel needs | NVLink inside a node |
| DL vs ML difference | DL learns features automatically |
| Clustering without labels | Unsupervised |
| Next-token pre-training | Self-supervised |
| Key 2017 architecture | Transformer |
| Recommenders | Merlin |
| Speech AI | Riva |
| Video analytics | Metropolis |
| Cybersecurity AI | Morpheus |
| Healthcare AI | Clara |
| Robotics | Isaac |
| Digital twins | Omniverse |
| MIG + TF32 introduced in | Ampere (A100) |
| FP8 + Transformer Engine introduced in | Hopper (H100) |
| FP4 introduced in | Blackwell |
| DGX vs HGX | Full system vs OEM GPU board |
| Low-power inference GPU | L4 (72 W) |
| Warp size | 32 threads |
| GPU matrix unit | Tensor Core |
| GPU memory type | HBM |
| Amdahl 20% serial → max speedup | 5x |

## Domain 2

| Front | Back |
|---|---|
| DGX H100 GPU memory | 640 GB |
| DGX H100 power | ~10.2 kW |
| DGX B200 power | ~14.3 kW |
| DGX H100 compute NICs | 8 × 400 Gb/s ConnectX-7 |
| SuperPOD scalable unit | 32 DGX nodes |
| PUE formula | Facility ÷ IT |
| Best PUE | Closest to 1.0 |
| 1 W in BTU/hr | 3.412 |
| 2N | Two independent full power paths |
| Liquid cooling needed for | GB200 NVL72, > ~40 kW/rack |
| Concurrently maintainable tier | Tier III |
| Short bursty demand | Cloud |
| Buying hardware | CapEx |
| Data gravity | Compute moves to data |
| 4 cluster networks | Compute, storage, in-band, OOB |
| NIC ↔ GPU memory directly | GPUDirect RDMA |
| Storage ↔ GPU memory directly | GPUDirect Storage |
| In-switch reductions | SHARP |
| IB lossless mechanism | Credit-based flow control |
| IB routing + LIDs | Subnet Manager |
| RDMA over UDP/IP | RoCE v2 |
| Lossless Ethernet | PFC + ECN |
| NDR | 400 Gb/s |
| XDR | 800 Gb/s |
| 400 Gb/s in GB/s | 50 |
| H100 NVLink per GPU | 900 GB/s |
| B200 NVLink per GPU | 1.8 TB/s |
| Grace ↔ GPU link | NVLink-C2C |
| AI Ethernet platform | Spectrum-X |
| DPU SDK | DOCA |
| DPU main jobs | Offload networking, storage, security; isolate |
| Training fabric oversubscription | 1:1 non-blocking |
| Rail-optimized | NIC n → leaf n |

## Domain 3

| Front | Back |
|---|---|
| Reboot frozen node remotely | BMC (IPMI/Redfish) |
| REST API for BMC | Redfish |
| Cluster provisioning | Base Command Manager |
| IB fabric monitoring | UFM |
| GPU telemetry tool | DCGM |
| DCGM Exporter port | 9400 |
| Long DCGM diagnostic | `dcgmi diag -r 3` |
| Better than GPU_UTIL | SM_ACTIVE |
| Hot + low clock | Thermal throttling |
| XID 48 | Double-bit ECC |
| XID 74 | NVLink error |
| XID 79 | Fell off the bus |
| Corrected ECC | Single-bit |
| List Slurm nodes | `sinfo` |
| List Slurm jobs | `squeue` |
| Submit Slurm batch | `sbatch` |
| Stop new jobs on node | Drain |
| Containers in Slurm | Pyxis + Enroot |
| K8s GPU resource | `nvidia.com/gpu` |
| Makes GPUs visible to K8s | Device plugin |
| GPU node labels | GPU Feature Discovery |
| Fractional GPUs + quotas | Run:ai |
| Max MIG instances | 7 |
| No-isolation sharing | Time-slicing |
| VMs with GPUs | vGPU (hypervisor + license) |
| `2g.20gb` | 2 compute slices, 20 GB |
| Enable MIG | `nvidia-smi -i 0 -mig 1` |
