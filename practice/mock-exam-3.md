# NCA-AIIO Mock Exam 3

**50 questions · 60 minutes · weighted 38% / 40% / 22% like the real exam.**

Rules: set a 60-minute timer. Write your answers on paper. Do not open the answer key until you finish.
Interactive version: `python practice/quiz.py --exam 3`

### Q1. Which library implements optimized all-reduce, all-gather, and broadcast operations across GPUs and nodes?

- A. cuBLAS
- B. DOCA
- C. NCCL
- D. TensorRT-LLM

### Q2. What does NVIDIA NIM provide?

- A. A GPU health diagnostic tool
- B. Prebuilt inference microservices that package a model, an optimized engine, and a standard API
- C. A cluster provisioning system for bare-metal nodes
- D. A DPU programming SDK

### Q3. Why does training a model need much more GPU memory than running inference on the same model?

- A. Training stores gradients, optimizer states, and activations in addition to the weights
- B. Training always uses FP64 precision
- C. Inference loads the model on the CPU
- D. Training models have more layers

### Q4. In large-scale distributed training, which traffic pattern dominates the cluster network?

- A. North-south traffic from users
- B. Out-of-band BMC traffic
- C. DNS traffic
- D. East-west GPU-to-GPU traffic such as gradient all-reduce

### Q5. Which statement correctly describes the relationship between AI, ML, and DL?

- A. ML is a subset of DL, which is a subset of AI
- B. AI is a subset of ML
- C. DL is a subset of ML, which is a subset of AI
- D. They are unrelated fields

### Q6. An expert system makes decisions with if-then rules written by people. How is it classified?

- A. Deep learning
- B. AI, but not machine learning
- C. Supervised machine learning
- D. Generative AI

### Q7. Which hardware development was the largest enabler of the deep learning breakthrough after 2012?

- A. GPU-accelerated parallel computing
- B. Faster single-core CPU clock speeds
- C. Magnetic tape storage
- D. Larger hard disk drives

### Q8. Which combination of factors best explains the rapid improvement of AI in the last decade?

- A. Smaller datasets and simpler models
- B. Mainframe computing and batch processing
- C. Proprietary closed frameworks only
- D. Accelerated computing, large datasets, better algorithms, and an open software ecosystem

### Q9. A contact center needs speech recognition, text-to-speech, and translation. Which NVIDIA SDK fits?

- A. NVIDIA Morpheus
- B. NVIDIA Metropolis
- C. NVIDIA Riva
- D. NVIDIA DRIVE

### Q10. Which NVIDIA platform is used to build physically accurate 3D simulations and digital twins of factories?

- A. NVIDIA Riva
- B. NVIDIA Omniverse
- C. NVIDIA DALI
- D. NVIDIA NCCL

### Q11. What is the main difference between NVIDIA DGX and NVIDIA HGX?

- A. DGX is a complete NVIDIA-built AI system; HGX is a GPU baseboard platform that OEM partners build servers around
- B. HGX is a cloud service; DGX is a CPU
- C. DGX supports only inference; HGX supports only training
- D. There is no difference

### Q12. Which NVIDIA architecture added FP4 precision support in its second-generation Transformer Engine?

- A. Ampere
- B. Hopper
- C. Ada Lovelace
- D. Blackwell

### Q13. A company needs an energy-efficient, low-profile GPU for large-scale video AI and inference in mainstream servers. Which GPU fits best?

- A. H200
- B. B200
- C. L4
- D. GB200

### Q14. Which NVIDIA cloud service deploys and manages AI applications across many remote edge locations, such as retail stores?

- A. NVIDIA NeMo
- B. NVIDIA Fleet Command
- C. NVIDIA cuDNN
- D. NVIDIA UFM

### Q15. In the AI life cycle, in which stage is TensorRT typically used?

- A. Optimization of a trained model before deployment
- B. Data labeling
- C. Data collection
- D. Facility planning

### Q16. Which NVIDIA framework is used to build, customize, and fine-tune large language models?

- A. NVIDIA DALI
- B. NVIDIA DCGM
- C. NVIDIA Metropolis
- D. NVIDIA NeMo

### Q17. How many threads are in an NVIDIA GPU warp?

- A. 8
- B. 16
- C. 32
- D. 64

### Q18. Which memory technology gives data center GPUs much higher memory bandwidth than typical CPU system memory?

- A. DDR4
- B. HBM (High Bandwidth Memory)
- C. NAND flash
- D. Optane

### Q19. A program is 80% parallel and 20% serial. What is the maximum theoretical speedup with unlimited parallel processors (Amdahl's law)?

- A. 5x
- B. 10x
- C. 20x
- D. Unlimited

### Q20. A full fine-tune of a model needs about 1.1 TB of GPU memory. Which configuration is the minimum that can hold it?

- A. One H100 80 GB GPU
- B. One DGX H100
- C. One L40S
- D. Two or more DGX H100 nodes connected with a high-speed fabric

### Q21. What is the approximate maximum power consumption of a DGX B200 system?

- A. ~3 kW
- B. ~6.5 kW
- C. ~10.2 kW
- D. ~14.3 kW

### Q22. 8 GPUs process 680 images/s. One GPU processes 100 images/s. What is the scaling efficiency?

- A. 68%
- B. 80%
- C. 85%
- D. 100%

### Q23. What is the benefit of a rail-optimized network topology in a GPU cluster?

- A. It removes the need for switches
- B. GPUs with the same local index on different nodes are one leaf-switch hop apart, which reduces latency and congestion
- C. It isolates management traffic
- D. It reduces power consumption of GPUs

### Q24. Approximately how much power does a rack with four DGX H100 systems need at full load?

- A. ~41 kW
- B. ~10 kW
- C. ~20 kW
- D. ~120 kW

### Q25. What is the purpose of hot aisle / cold aisle containment?

- A. To increase server noise
- B. To store spare parts
- C. To reduce cable length
- D. To keep hot exhaust air and cold supply air separate so cooling is more efficient

### Q26. Buying DGX systems is an example of which type of expenditure?

- A. OpEx
- B. Subscription
- C. CapEx
- D. Egress

### Q27. What helps workloads move between on-prem and cloud in a hybrid strategy?

- A. Different software stacks in each location
- B. A consistent software stack, such as containers from NGC, Kubernetes, and NVIDIA AI Enterprise
- C. Using only bare-metal installs
- D. Avoiding containers

### Q28. Which technology moves data directly between storage and GPU memory without a bounce buffer in CPU memory?

- A. GPUDirect Storage
- B. NVLink-C2C
- C. MIG
- D. PCIe ACS

### Q29. Which NVIDIA software manages and monitors an InfiniBand fabric, including the subnet manager function?

- A. DCGM
- B. Triton
- C. DOCA
- D. UFM (Unified Fabric Manager)

### Q30. Which Uptime Institute tier describes a data center that is concurrently maintainable?

- A. Tier I
- B. Tier II
- C. Tier III
- D. Tier 0

### Q31. What heat load must the cooling system remove for 10 kW of IT equipment?

- A. ~3,412 BTU/hr
- B. ~34,120 BTU/hr
- C. ~12,000 BTU/hr
- D. ~1,000 BTU/hr

### Q32. Convert 400 Gb/s to GB/s.

- A. 50 GB/s
- B. 400 GB/s
- C. 3.2 GB/s
- D. 100 GB/s

### Q33. Which traffic type mainly reaches an inference service from clients outside the cluster?

- A. East-west
- B. NVLink
- C. Out-of-band
- D. North-south

### Q34. What is RoCE v2?

- A. A GPU memory type
- B. A cooling standard
- C. RDMA over Converged Ethernet that is encapsulated in UDP/IP and is routable
- D. An InfiniBand speed grade

### Q35. What is NVIDIA Spectrum-X?

- A. An InfiniBand subnet manager
- B. An AI-optimized Ethernet platform combining Spectrum-4 switches and BlueField-3 SuperNICs
- C. A GPU architecture
- D. A cooling system

### Q36. Which link connects the Grace CPU and the GPU inside a GH200 Grace Hopper Superchip?

- A. NVLink-C2C
- B. PCIe Gen4
- C. InfiniBand
- D. Ethernet

### Q37. What does 'VPI' mean for a ConnectX adapter?

- A. Video processing interface
- B. Virtual private interconnect
- C. Voltage protection indicator
- D. Virtual Protocol Interconnect: the port can run InfiniBand or Ethernet

### Q38. Why does running a firewall on a DPU improve security compared with running it on the host?

- A. DPUs have faster GPUs
- B. DPUs do not use networks
- C. The DPU is a separate trust domain, so a compromised host OS cannot disable the security controls
- D. Firewalls do not work on CPUs

### Q39. What is a key benefit of offloading software-defined networking (e.g., Open vSwitch) to a DPU?

- A. It increases GPU memory
- B. It frees host CPU cores for applications and accelerates packet processing
- C. It removes the need for switches
- D. It enables MIG

### Q40. Which NVIDIA software provisions OS images to cluster nodes and manages cluster configuration and workload managers?

- A. NVIDIA TensorRT
- B. NVIDIA Riva
- C. NVIDIA Base Command Manager
- D. NVIDIA Merlin

### Q41. Which tool is used to manage data center facilities such as power, cooling, space, and assets?

- A. NCCL
- B. DCIM (Data Center Infrastructure Management)
- C. DALI
- D. NeMo

### Q42. Which scheduler is traditionally used for large multi-node batch training and HPC jobs on GPU clusters?

- A. Slurm
- B. Docker Compose
- C. cron
- D. systemd

### Q43. Which Slurm command shows the state of partitions and nodes?

- A. squeue
- B. sbatch
- C. scancel
- D. sinfo

### Q44. Which Slurm plugins let users run NGC container images as part of their jobs?

- A. Helm and Kustomize
- B. Prometheus and Alertmanager
- C. Pyxis and Enroot
- D. Kubeflow and MLflow

### Q45. What is the main advantage of containers compared with virtual machines for AI workloads?

- A. Containers include a full guest OS kernel
- B. Containers are lightweight, share the host kernel, and package the application and its libraries consistently
- C. Containers cannot use GPUs
- D. Containers need a hypervisor

### Q46. An H100 shows 88 °C temperature and SM clocks well below maximum under load. What is the most likely issue?

- A. Thermal throttling
- B. MIG misconfiguration
- C. Low PCIe bandwidth
- D. Driver too new

### Q47. Which command runs an extended DCGM diagnostic on GPUs before returning a node to service?

- A. nvidia-smi -L
- B. dcgmi discovery -l
- C. sinfo -R
- D. dcgmi diag -r 3

### Q48. What is the maximum number of MIG GPU instances on an NVIDIA H100?

- A. 2
- B. 4
- C. 7
- D. 16

### Q49. What does the MIG profile name '3g.40gb' mean?

- A. 3 GPUs with 40 GB each
- B. 3 compute slices and 40 GB of GPU memory
- C. 3rd generation GPU with 40 GB
- D. 3 GB of memory and 40 compute units

### Q50. What must be done before creating MIG instances on a supported GPU?

- A. Enable MIG mode on the GPU (nvidia-smi -mig 1), which requires a GPU reset
- B. Install Slurm
- C. Disable ECC
- D. Connect an NVLink bridge

---

## Answer key

<details><summary>Show answers (only after you finish)</summary>

| Q | Answer | Topic | Why |
|---|---|---|---|
| 1 | **C** | 1.1 | NCCL (NVIDIA Collective Communications Library) provides multi-GPU, multi-node collectives over NVLink, PCIe, InfiniBand, and RoCE. |
| 2 | **B** | 1.1 | NIM microservices are containers with optimized models and industry-standard APIs, part of NVIDIA AI Enterprise. |
| 3 | **A** | 1.2 | Mixed-precision training with Adam needs roughly 16 bytes per parameter plus activations, versus ~2 bytes per parameter for FP16 inference. |
| 4 | **D** | 1.2 | Distributed training synchronizes gradients between GPUs across nodes, which is east-west traffic. |
| 5 | **C** | 1.3 | Deep learning is a type of machine learning; machine learning is a type of AI. |
| 6 | **B** | 1.3 | Rule-based systems are AI but do not learn from data, so they are not ML. |
| 7 | **A** | 1.4 | GPUs made training large neural networks practical (e.g., AlexNet on GPUs). |
| 8 | **D** | 1.4 | These forces reinforce each other. |
| 9 | **C** | 1.5 | Riva is NVIDIA's speech AI SDK. |
| 10 | **B** | 1.5 | Omniverse is NVIDIA's platform for 3D simulation and digital twins based on OpenUSD. |
| 11 | **A** | 1.6 | DGX is NVIDIA's full-stack system; HGX is the 8-GPU board (GPUs + NVSwitch) used by OEMs. |
| 12 | **D** | 1.6 | Blackwell (B200/GB200) added FP4. |
| 13 | **C** | 1.6 | L4 is a low-power (72 W) PCIe GPU for efficient inference and video. |
| 14 | **B** | 1.6 | Fleet Command manages edge AI deployments centrally. |
| 15 | **A** | 1.7 | TensorRT optimizes trained models for inference. |
| 16 | **D** | 1.7 | NeMo is NVIDIA's framework for building and customizing generative AI models. |
| 17 | **C** | 1.8 | A warp is 32 threads that execute the same instruction (SIMT). |
| 18 | **B** | 1.8 | HBM stacks provide multiple TB/s of bandwidth (e.g., H100 ~3.35 TB/s, B200 ~8 TB/s). |
| 19 | **A** | 1.8 | Max speedup = 1 / serial fraction = 1 / 0.2 = 5x. |
| 20 | **D** | 2.1 | One DGX H100 has 640 GB, so 1.1 TB needs at least two nodes (or memory-saving methods). |
| 21 | **D** | 2.1 | DGX B200 is rated ~14.3 kW max; DGX H100 ~10.2 kW; DGX A100 ~6.5 kW. |
| 22 | **C** | 2.2 | 680 / (8 x 100) = 85%. |
| 23 | **B** | 2.2 | NIC n of every node connects to the rail-n leaf switch. |
| 24 | **A** | 2.3 | 4 x ~10.2 kW ≈ 41 kW. |
| 25 | **D** | 2.3 | Containment prevents mixing of hot and cold air. |
| 26 | **C** | 2.4 | Purchasing hardware is capital expenditure. |
| 27 | **B** | 2.4 | A common stack makes workloads portable. |
| 28 | **A** | 2.5 | GPUDirect Storage provides a direct DMA path between storage and GPU memory. |
| 29 | **D** | 2.5 | UFM manages InfiniBand fabrics. |
| 30 | **C** | 2.6 | Tier III allows maintenance of any component without shutting down IT. |
| 31 | **B** | 2.6 | 1 W = 3.412 BTU/hr, so 10 kW ≈ 34,120 BTU/hr (≈ 2.8 tons). |
| 32 | **A** | 2.7 | Divide bits by 8: 400 / 8 = 50 GB/s. |
| 33 | **D** | 2.7 | Client requests enter and leave the data center: north-south. |
| 34 | **C** | 2.8 | RoCE v2 runs RDMA over UDP/IP; RoCE v1 is Layer 2 only. |
| 35 | **B** | 2.8 | Spectrum-X brings adaptive routing and congestion control to Ethernet for AI. |
| 36 | **A** | 2.9 | NVLink-C2C provides 900 GB/s coherent CPU-GPU bandwidth. |
| 37 | **D** | 2.9 | VPI adapters support both InfiniBand and Ethernet. |
| 38 | **C** | 2.10 | DPU-based isolation supports zero-trust architectures. |
| 39 | **B** | 2.10 | Offload returns CPU cycles to applications and improves performance. |
| 40 | **C** | 3.1 | Base Command Manager (formerly Bright Cluster Manager) handles provisioning and cluster management. |
| 41 | **B** | 3.1 | DCIM covers facility-level monitoring and capacity planning. |
| 42 | **A** | 3.2 | Slurm is the standard HPC workload manager. |
| 43 | **D** | 3.2 | sinfo shows partitions and node states; squeue shows jobs. |
| 44 | **C** | 3.2 | Pyxis (SPANK plugin) + Enroot run containers in Slurm. |
| 45 | **B** | 3.2 | Containers are portable and lightweight. |
| 46 | **A** | 3.3 | High temperature plus reduced clocks indicates thermal throttling. |
| 47 | **D** | 3.3 | Run level 3 is the long diagnostic (level 1 quick, level 2 medium). |
| 48 | **C** | 3.4 | MIG supports up to 7 instances on A100/H100/H200/B200. |
| 49 | **B** | 3.4 | Format: <compute slices>g.<memory>gb. |
| 50 | **A** | 3.4 | MIG mode must be enabled first, then GPU and compute instances are created. |

</details>

**Score guide:** 40+/50 (80%) = ready. 35–39 = review weak topics. Below 35 = repeat the study plan week for weak domains.
