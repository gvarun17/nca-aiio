# Glossary

| Term | Meaning |
|---|---|
| **Activation** | Output of a layer. Stored during training for the backward pass. |
| **All-reduce** | Collective operation: every GPU ends with the sum/average of all GPUs' data. Used to sync gradients. |
| **Amdahl's law** | Max speedup = 1 ÷ serial fraction. |
| **BasePOD** | NVIDIA reference architecture for small/medium DGX clusters. |
| **Backfill** | Scheduler runs small jobs in gaps without delaying high-priority jobs. |
| **BF16** | 16-bit floating point with FP32's range. Common for training. |
| **BlueField** | NVIDIA DPU: ConnectX NIC + Arm cores + accelerators. |
| **BMC** | Baseboard Management Controller. Out-of-band hardware management. |
| **CDU** | Coolant Distribution Unit for liquid cooling. |
| **ConnectX** | NVIDIA network adapter family (InfiniBand/Ethernet). |
| **CUDA** | NVIDIA parallel computing platform and programming model. |
| **cuDNN** | CUDA library of deep learning primitives. |
| **DALI** | Data Loading Library: GPU data decoding and augmentation. |
| **Data parallel** | Each GPU has the full model and a part of the data. |
| **DCGM** | Data Center GPU Manager: telemetry, health, diagnostics. |
| **DCQCN** | Congestion control for RoCE based on ECN. |
| **DGX** | NVIDIA's complete AI system (e.g., DGX B200). |
| **DOCA** | SDK for BlueField DPUs. |
| **DPU** | Data Processing Unit: offloads networking, storage, security. |
| **Drain** | Scheduler state: no new jobs on the node. |
| **East-west traffic** | Traffic between servers inside the data center. |
| **ECC (SBE/DBE)** | Memory error correction. Single-bit corrected; double-bit uncorrectable. |
| **ECN** | Explicit Congestion Notification. |
| **Fat-tree / leaf-spine** | Multi-path network topology with equal-cost paths. |
| **FP8 / FP4** | 8-bit / 4-bit floating point for fast AI math (Hopper / Blackwell). |
| **GPU Feature Discovery** | Labels Kubernetes nodes with GPU properties. |
| **GPU Operator** | Kubernetes operator that installs all GPU software components. |
| **GPUDirect RDMA** | NIC reads/writes GPU memory directly. |
| **GPUDirect Storage** | Storage reads/writes GPU memory directly. |
| **Grace** | NVIDIA Arm data center CPU. |
| **HBM** | High Bandwidth Memory on GPU packages. |
| **HCA** | Host Channel Adapter (InfiniBand NIC). |
| **HGX** | NVIDIA GPU baseboard platform for OEM servers. |
| **InfiniBand** | Low-latency, lossless, RDMA-native network. |
| **IPMI** | Older protocol for BMC management. |
| **KV cache** | Stored attention keys/values during LLM inference. |
| **LID** | Local Identifier: InfiniBand address set by the Subnet Manager. |
| **MIG** | Multi-Instance GPU: up to 7 hardware-isolated instances. |
| **MLOps** | Practices to automate the ML life cycle. |
| **MPS** | Multi-Process Service: concurrent CUDA processes on a GPU. |
| **NCCL** | NVIDIA Collective Communications Library. |
| **NeMo** | Framework to build and customize generative AI models. |
| **NGC** | NVIDIA catalog of GPU-optimized software (`nvcr.io`). |
| **NIM** | NVIDIA Inference Microservices. |
| **North-south traffic** | Traffic into and out of the data center. |
| **NVLink** | High-speed GPU-to-GPU link. |
| **NVLink-C2C** | Chip-to-chip link between Grace CPU and GPU. |
| **NVSwitch** | Switch chip that connects NVLinks all-to-all. |
| **OOB network** | Out-of-band management network (BMCs). |
| **Oversubscription** | Downlink bandwidth greater than uplink bandwidth. |
| **PFC** | Priority Flow Control: pauses a traffic class to prevent drops. |
| **Pipeline parallel** | Split model layers into stages on different GPUs. |
| **PUE** | Power Usage Effectiveness = facility power ÷ IT power. |
| **Pyxis / Enroot** | Run containers in Slurm jobs. |
| **Rail-optimized** | NIC *n* of every node connects to leaf switch *n*. |
| **RAPIDS** | GPU data science libraries (cuDF, cuML). |
| **RDMA** | Remote Direct Memory Access. |
| **Redfish** | REST API for BMC management. |
| **RoCE v2** | RDMA over Converged Ethernet (UDP/IP, routable). |
| **Run:ai** | Kubernetes GPU orchestration (quotas, fractions). |
| **SHARP** | In-network reductions in InfiniBand switches. |
| **Slurm** | HPC workload manager. |
| **SM** | Streaming Multiprocessor. |
| **Spectrum-X** | NVIDIA AI Ethernet platform. |
| **Subnet Manager** | Configures and routes an InfiniBand fabric. |
| **SuperPOD** | Large-scale DGX reference architecture built from scalable units. |
| **Tensor Core** | GPU unit for matrix multiply-accumulate. |
| **Tensor parallel** | Split each layer across GPUs. |
| **TensorRT** | Inference optimizer and runtime. |
| **Time-slicing** | GPU sharing by context switching; no isolation. |
| **Triton** | NVIDIA inference server (part of Dynamo). |
| **UFM** | Unified Fabric Manager for InfiniBand. |
| **vGPU** | Virtual GPUs for VMs through a hypervisor (licensed). |
| **Warp** | 32 threads executing together. |
| **XID** | NVIDIA driver error code in the kernel log. |
