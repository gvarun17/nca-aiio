# NCA-AIIO Mock Exam 1

**50 questions · 60 minutes · weighted 38% / 40% / 22% like the real exam.**

Rules: set a 60-minute timer. Write your answers on paper. Do not open the answer key until you finish.
Interactive version: `python practice/quiz.py --exam 1`

### Q1. Which NVIDIA component optimizes a trained neural network for inference through layer fusion, precision calibration, and kernel auto-tuning?

- A. Triton Inference Server
- B. TensorRT
- C. NCCL
- D. cuDNN

### Q2. Where would an engineer download a GPU-optimized, tested PyTorch container from NVIDIA?

- A. NVIDIA Fleet Command
- B. NVIDIA Base Command Manager
- C. NVIDIA DOCA
- D. NVIDIA NGC catalog

### Q3. Which offering provides enterprise support, security updates, and a licensed suite of NVIDIA AI software such as NIM, NeMo, RAPIDS, and Triton?

- A. NVIDIA NGC public catalog only
- B. CUDA Toolkit
- C. NVIDIA AI Enterprise
- D. NVIDIA Omniverse

### Q4. A real-time fraud detection system must score each card transaction quickly. Which metric is MOST important?

- A. Time to train
- B. Inference latency
- C. Number of training epochs
- D. Checkpoint size

### Q5. Which parallelism strategy splits each layer of a model across GPUs and therefore needs the fastest interconnect, usually NVLink inside a node?

- A. Tensor parallelism
- B. Data parallelism
- C. Hyperparameter sweeps
- D. Pipeline of independent jobs

### Q6. What is the main difference between classic machine learning and deep learning?

- A. Classic ML always needs GPUs
- B. Deep learning cannot use labeled data
- C. Classic ML uses neural networks with many layers
- D. Deep learning learns features automatically from raw data, while classic ML usually depends on manual feature engineering

### Q7. Why is deep learning well suited to GPUs?

- A. Neural networks need branch prediction
- B. Deep learning uses mostly serial operations
- C. Neural network layers are dominated by highly parallel matrix multiplications
- D. GPUs have larger caches than CPUs

### Q8. Which 2017 neural network architecture, based on attention, is the foundation of modern large language models?

- A. Convolutional neural network
- B. Transformer
- C. Recurrent neural network
- D. Decision tree ensemble

### Q9. What do AI 'scaling laws' describe?

- A. Predictable model quality improvements when compute, data, and model size increase together
- B. Rules for scaling data center floor space
- C. Licensing tiers for AI software
- D. Limits on the number of GPUs per server

### Q10. A city wants AI video analytics for traffic flow and safety from thousands of cameras. Which NVIDIA platform is most relevant?

- A. NVIDIA Merlin
- B. NVIDIA BioNeMo
- C. NVIDIA Morpheus
- D. NVIDIA Metropolis

### Q11. Which NVIDIA framework is designed for AI-based cybersecurity, such as detecting anomalies in network traffic in real time?

- A. NVIDIA Maxine
- B. NVIDIA Clara
- C. NVIDIA Morpheus
- D. NVIDIA Isaac

### Q12. Which GPU architecture introduced Multi-Instance GPU (MIG) and TF32 Tensor Core support?

- A. Hopper
- B. Ampere
- C. Pascal
- D. Blackwell

### Q13. What is the NVIDIA Grace CPU?

- A. An Arm-based data center CPU designed by NVIDIA
- B. An x86 server CPU
- C. A DPU
- D. A network switch

### Q14. Which offering gives access to NVIDIA's AI platform and DGX-class infrastructure hosted in partner public clouds?

- A. NVIDIA Jetson
- B. NVIDIA IGX
- C. NVIDIA BlueField
- D. NVIDIA DGX Cloud

### Q15. GPUs are underutilized during image model training because JPEG decoding and augmentation on the CPU are slow. Which NVIDIA library helps?

- A. NCCL
- B. TensorRT
- C. DALI
- D. DOCA

### Q16. What is model drift?

- A. Moving a model between GPUs
- B. A decline in model accuracy because production data changes over time
- C. A GPU clock speed change
- D. A change in container image tags

### Q17. Why do teams use containers from NGC across development, training, and deployment?

- A. They provide consistent, tested software stacks that run the same way on different GPU systems
- B. They remove the need for GPU drivers
- C. They make models more accurate
- D. They replace the scheduler

### Q18. Which GPU unit is specialized for matrix multiply-accumulate operations used in deep learning?

- A. Raster engine
- B. Video decoder
- C. Copy engine
- D. Tensor Core

### Q19. Which workload is a CPU generally better suited for than a GPU?

- A. Training a transformer
- B. Large matrix multiplication
- C. Serial code with complex branching and control logic
- D. Rendering millions of pixels

### Q20. How much total GPU memory does an NVIDIA DGX H100 system provide?

- A. 320 GB
- B. 640 GB
- C. 1,440 GB
- D. 80 GB

### Q21. Why are SXM-form-factor GPUs used in DGX and HGX systems instead of PCIe cards for large-scale training?

- A. SXM supports full NVLink/NVSwitch connectivity and higher power limits
- B. SXM GPUs do not need cooling
- C. SXM GPUs are cheaper
- D. PCIe GPUs cannot run CUDA

### Q22. What is the building block of the NVIDIA DGX SuperPOD reference architecture for DGX H100 and B200?

- A. A scalable unit (SU) of 32 DGX systems
- B. A single DGX system
- C. A pod of 4 GPUs
- D. A rack of 72 CPUs

### Q23. Which term describes adding more nodes connected over a network to increase cluster capacity?

- A. Scale up
- B. Overclocking
- C. Time-slicing
- D. Scale out

### Q24. A facility uses 1,500 kW in total and its IT equipment uses 1,200 kW. What is the PUE?

- A. 0.80
- B. 1.20
- C. 1.25
- D. 1.50

### Q25. Which cooling method is required for very high-density racks such as the GB200 NVL72?

- A. Room air conditioning without containment
- B. Direct liquid cooling
- C. Open windows
- D. Raised floor only

### Q26. A research team needs 128 GPUs for a one-month experiment and then no GPUs. Which option is usually best?

- A. Cloud GPU instances
- B. Buy a DGX SuperPOD
- C. Build a new data center
- D. Use CPU-only servers

### Q27. What does 'data gravity' mean in infrastructure planning?

- A. Data stored on heavy disks
- B. Gravity-based cooling
- C. Data replication across regions
- D. Large datasets are hard and costly to move, so compute is placed near the data

### Q28. In a DGX SuperPOD, which network carries GPU-to-GPU traffic between nodes during distributed training?

- A. Out-of-band management network
- B. In-band management network
- C. Compute fabric
- D. Storage fabric

### Q29. Which type of storage is typically used to feed large training jobs on many nodes?

- A. A single USB disk
- B. A high-performance parallel file system
- C. Tape library only
- D. Each user's laptop

### Q30. A data center can supply and cool only 20 kW per rack. How should DGX H100 systems be deployed?

- A. Deploy one system per rack and use more racks
- B. Put four systems per rack
- C. Remove power supplies from each system
- D. Disable cooling fans

### Q31. Which item is required by direct liquid cooling but not by air cooling?

- A. Blanking panels
- B. Rack PDU
- C. Hot aisle
- D. Coolant distribution unit (CDU) and facility water loop

### Q32. Which feature allows a network adapter to read and write GPU memory directly, bypassing CPU system memory?

- A. GPU Boost
- B. SR-IOV
- C. GPUDirect RDMA
- D. NVENC

### Q33. Which InfiniBand feature performs data reduction operations inside the network switches to accelerate collectives?

- A. PFC
- B. SHARP
- C. ECMP
- D. VXLAN

### Q34. In an InfiniBand fabric, which component discovers the topology, assigns local identifiers (LIDs), and computes routes?

- A. Subnet Manager
- B. DHCP server
- C. BGP router
- D. DNS server

### Q35. Which Ethernet mechanisms are configured to make RoCE traffic lossless and control congestion?

- A. STP and LACP
- B. NAT and DHCP
- C. VRRP and HSRP
- D. PFC and ECN

### Q36. Which interconnect provides the highest bandwidth between GPUs inside a DGX H100?

- A. PCIe Gen5
- B. 100 GbE
- C. NVLink with NVSwitch
- D. InfiniBand HDR

### Q37. What is the per-GPU NVLink bandwidth of a Blackwell B200 GPU (fifth-generation NVLink)?

- A. 300 GB/s
- B. 1.8 TB/s
- C. 600 GB/s
- D. 64 GB/s

### Q38. What is the primary purpose of a DPU such as NVIDIA BlueField?

- A. Offload, accelerate, and isolate infrastructure tasks such as networking, storage, and security
- B. Train neural networks
- C. Replace the GPU
- D. Provide graphics output

### Q39. Which components are part of a BlueField DPU?

- A. Tensor Cores and HBM only
- B. A GPU and a display controller
- C. Only a PHY chip
- D. A ConnectX network adapter, Arm cores, and hardware accelerators

### Q40. Which component lets an administrator power-cycle a server and view its console even when the operating system has crashed?

- A. Baseboard Management Controller (BMC)
- B. DCGM
- C. Slurm controller
- D. Triton

### Q41. A common monitoring stack collects GPU metrics as time series and displays dashboards and alerts. Which pair is typically used?

- A. Slurm and Enroot
- B. NCCL and UFM
- C. Redfish and IPMI
- D. Prometheus and Grafana

### Q42. A node reports a hardware GPU error. What should the operator do FIRST in the scheduler?

- A. Delete all user accounts
- B. Increase job priority
- C. Drain the node so no new jobs start on it
- D. Reboot all nodes in the cluster

### Q43. In Kubernetes, which resource name does a pod request to get one full NVIDIA GPU?

- A. gpu.nvidia/count
- B. nvidia.com/gpu
- C. cuda/device
- D. k8s.io/accelerator

### Q44. Which Slurm scheduling feature lets small jobs start earlier in idle gaps without delaying higher-priority jobs?

- A. Backfill
- B. Preemption
- C. Fair-share decay
- D. Job arrays

### Q45. Which workload is a better fit for Kubernetes than for Slurm?

- A. A tightly coupled MPI weather simulation
- B. A one-time batch benchmark
- C. A large multi-node pre-training batch job
- D. A long-running, autoscaled inference microservice

### Q46. Which NVIDIA tool provides GPU health checks, diagnostics, and telemetry at data center scale?

- A. NCCL
- B. TensorRT
- C. DCGM (Data Center GPU Manager)
- D. DALI

### Q47. What does XID 79 in the kernel log indicate?

- A. An application illegal memory access
- B. The GPU has fallen off the bus
- C. A normal driver load
- D. A completed job

### Q48. On which default port does NVIDIA DCGM Exporter publish Prometheus metrics?

- A. 9400
- B. 8080
- C. 3000
- D. 22

### Q49. Which GPU sharing method provides NO memory or fault isolation between workloads?

- A. MIG
- B. GPU passthrough
- C. vGPU with MIG backing
- D. Time-slicing

### Q50. Which requirements are specific to NVIDIA vGPU compared with MIG on bare metal?

- A. A Kubernetes cluster and Helm
- B. An InfiniBand fabric
- C. A supported hypervisor and an NVIDIA software license
- D. A liquid-cooled rack

---

## Answer key

<details><summary>Show answers (only after you finish)</summary>

| Q | Answer | Topic | Why |
|---|---|---|---|
| 1 | **B** | 1.1 | TensorRT is the inference optimizer/compiler. Triton serves models; NCCL handles communication; cuDNN provides DL primitives. |
| 2 | **D** | 1.1 | NGC is NVIDIA's catalog of GPU-optimized containers, models, and Helm charts (registry nvcr.io). |
| 3 | **C** | 1.1 | NVIDIA AI Enterprise is the supported, licensed software platform. |
| 4 | **B** | 1.2 | Online fraud scoring is a latency-sensitive inference workload. |
| 5 | **A** | 1.2 | Tensor parallelism communicates inside every layer, so it is kept within the NVLink domain. |
| 6 | **D** | 1.3 | Deep neural networks learn representations; classic ML often relies on engineered features. |
| 7 | **C** | 1.3 | Matrix math is massively parallel and maps well to thousands of GPU cores and Tensor Cores. |
| 8 | **B** | 1.4 | The Transformer architecture introduced attention-based models that power LLMs. |
| 9 | **A** | 1.4 | Scaling laws show loss decreasing predictably as compute, data, and parameters scale. |
| 10 | **D** | 1.5 | Metropolis (with DeepStream) targets vision AI and video analytics. |
| 11 | **C** | 1.5 | Morpheus is NVIDIA's AI framework for cybersecurity. |
| 12 | **B** | 1.6 | The Ampere A100 introduced MIG and TF32. |
| 13 | **A** | 1.6 | Grace is NVIDIA's Arm-based CPU, combined with GPUs in GH200/GB200 superchips. |
| 14 | **D** | 1.6 | DGX Cloud delivers NVIDIA's AI platform as a cloud service. |
| 15 | **C** | 1.7 | DALI moves data loading, decoding, and augmentation to the GPU. |
| 16 | **B** | 1.7 | MLOps monitors drift and triggers retraining. |
| 17 | **A** | 1.7 | Containers give reproducibility and portability. |
| 18 | **D** | 1.8 | Tensor Cores accelerate mixed-precision matrix math. |
| 19 | **C** | 1.8 | Serial, branch-heavy logic benefits from CPU features like branch prediction and large caches. |
| 20 | **B** | 2.1 | 8 x H100 80 GB = 640 GB. |
| 21 | **A** | 2.1 | SXM modules connect through NVSwitch for all-to-all NVLink and support higher TDP. |
| 22 | **A** | 2.2 | SuperPOD is built from scalable units of 32 DGX nodes. |
| 23 | **D** | 2.2 | Scale out adds nodes; scale up makes a node or NVLink domain bigger. |
| 24 | **C** | 2.3 | PUE = 1500 / 1200 = 1.25. |
| 25 | **B** | 2.3 | NVL72 racks are liquid-cooled; they exceed practical air-cooling limits. |
| 26 | **A** | 2.4 | Short-term, bursty demand favors cloud (OpEx, no long-term commitment). |
| 27 | **D** | 2.4 | Large data attracts applications and compute to its location. |
| 28 | **C** | 2.5 | The compute fabric (InfiniBand or Spectrum-X) carries east-west GPU traffic. |
| 29 | **B** | 2.5 | Parallel file systems (Lustre, IBM Storage Scale, WEKA, etc.) give shared high throughput. |
| 30 | **A** | 2.6 | Rack density must fit the power/cooling budget; ~10.2 kW per system. |
| 31 | **D** | 2.6 | DLC needs a CDU, a water loop, and leak detection. |
| 32 | **C** | 2.7 | GPUDirect RDMA removes extra copies through host memory. |
| 33 | **B** | 2.7 | SHARP offloads reductions to Quantum switches. |
| 34 | **A** | 2.8 | Every IB subnet needs an active Subnet Manager (OpenSM, switch-based, or UFM). |
| 35 | **D** | 2.8 | Priority Flow Control prevents drops; ECN (with DCQCN) signals congestion. |
| 36 | **C** | 2.9 | Fourth-generation NVLink gives 900 GB/s per H100 GPU through NVSwitch. |
| 37 | **B** | 2.9 | NVLink 5 provides 1.8 TB/s per GPU (Hopper: 900 GB/s). |
| 38 | **A** | 2.10 | The DPU runs data center infrastructure services so the host CPU focuses on applications. |
| 39 | **D** | 2.10 | BlueField combines ConnectX networking, Arm CPU cores, and accelerators. |
| 40 | **A** | 3.1 | The BMC provides out-of-band hardware management independent of the OS. |
| 41 | **D** | 3.1 | DCGM Exporter feeds Prometheus; Grafana visualizes. |
| 42 | **C** | 3.1 | Draining isolates the node while running jobs finish; then diagnose. |
| 43 | **B** | 3.2 | The NVIDIA device plugin advertises nvidia.com/gpu. |
| 44 | **A** | 3.2 | Backfill fills scheduling gaps. |
| 45 | **D** | 3.2 | Kubernetes is designed for services with deployments and autoscaling. |
| 46 | **C** | 3.3 | DCGM manages and monitors GPUs in clusters. |
| 47 | **B** | 3.3 | XID 79 is a serious hardware/PCIe event; drain, power-cycle, diagnose. |
| 48 | **A** | 3.3 | DCGM Exporter serves /metrics on port 9400. |
| 49 | **D** | 3.4 | Time-slicing shares the GPU by context switching without memory isolation. |
| 50 | **C** | 3.4 | vGPU runs in a hypervisor and needs licensing (e.g., through NVIDIA AI Enterprise for compute). |

</details>

**Score guide:** 40+/50 (80%) = ready. 35–39 = review weak topics. Below 35 = repeat the study plan week for weak domains.
