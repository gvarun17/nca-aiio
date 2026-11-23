# NCA-AIIO Mock Exam 2

**50 questions · 60 minutes · weighted 38% / 40% / 22% like the real exam.**

Rules: set a 60-minute timer. Write your answers on paper. Do not open the answer key until you finish.
Interactive version: `python practice/quiz.py --exam 2`

### Q1. A team must serve PyTorch, ONNX, and TensorRT models from one server with dynamic batching and HTTP/gRPC endpoints. Which software fits best?

- A. NVIDIA Triton Inference Server
- B. NVIDIA DALI
- C. NVIDIA RAPIDS
- D. NVIDIA DCGM

### Q2. In a containerized GPU environment, which component must be installed on the host rather than inside each container?

- A. The NVIDIA GPU driver
- B. cuDNN
- C. The CUDA runtime libraries
- D. PyTorch

### Q3. Which statement best describes inference compared with training?

- A. Inference needs forward and backward passes
- B. Inference updates model weights continuously
- C. Inference typically needs more memory per parameter than training
- D. Inference uses only the forward pass and focuses on latency and throughput

### Q4. Which precision formats are most commonly used to speed up inference on modern NVIDIA GPUs?

- A. FP64 only
- B. FP32 only
- C. FP8, INT8, and FP4
- D. Double-double precision

### Q5. A 7-billion-parameter model will run inference in FP16. Approximately how much GPU memory do the weights need?

- A. 7 GB
- B. 14 GB
- C. 28 GB
- D. 112 GB

### Q6. A model groups customers into segments using purchase data that has no labels. Which type of learning is this?

- A. Unsupervised learning
- B. Supervised learning
- C. Reinforcement learning
- D. Transfer learning

### Q7. Large language model pre-training that predicts the next token from unlabeled text is an example of which learning approach?

- A. Rule-based learning
- B. Reinforcement learning only
- C. Unsupervised clustering
- D. Self-supervised learning

### Q8. How has cloud computing contributed to AI adoption?

- A. It removed the need for GPUs
- B. It made all AI workloads cheaper at any scale
- C. It gave pay-as-you-go access to GPUs without large upfront investment
- D. It replaced open-source frameworks

### Q9. A retailer wants to show 'customers also bought' product suggestions. Which NVIDIA framework is designed for this?

- A. NVIDIA Riva
- B. NVIDIA Merlin
- C. NVIDIA Isaac
- D. NVIDIA Clara

### Q10. A company wants an LLM to answer questions using its internal documents without retraining the model. Which technique should it use?

- A. Retrieval-augmented generation (RAG)
- B. Full pre-training from scratch
- C. Reinforcement learning from games
- D. Image segmentation

### Q11. A hospital wants to use AI for medical image analysis. Which NVIDIA platform is designed for healthcare?

- A. NVIDIA DRIVE
- B. NVIDIA Merlin
- C. NVIDIA Spectrum-X
- D. NVIDIA Clara

### Q12. Which GPU architecture introduced the Transformer Engine with FP8 precision?

- A. Ampere
- B. Volta
- C. Hopper
- D. Turing

### Q13. Which rack-scale system connects 72 Blackwell GPUs and 36 Grace CPUs in one NVLink domain and uses liquid cooling?

- A. DGX H100
- B. GB200 NVL72
- C. DGX A100
- D. HGX H200

### Q14. Which NVIDIA platform is designed for embedded AI in robots, drones, and edge devices?

- A. NVIDIA Jetson
- B. NVIDIA DGX SuperPOD
- C. NVIDIA Quantum InfiniBand
- D. NVIDIA HGX

### Q15. Which NVIDIA suite accelerates data science and ETL with GPU versions of pandas and scikit-learn APIs?

- A. NVIDIA Riva
- B. NVIDIA Triton
- C. NVIDIA Merlin
- D. NVIDIA RAPIDS

### Q16. Which practice is part of MLOps but NOT normally part of traditional DevOps?

- A. Using source control for code
- B. Automated builds
- C. Versioning datasets and models and monitoring model accuracy
- D. Deploying containers

### Q17. Which statement best compares CPU and GPU design?

- A. CPUs have thousands of simple cores; GPUs have a few complex cores
- B. CPUs are optimized for low-latency serial work; GPUs are optimized for high-throughput parallel work
- C. GPUs are better for all workloads
- D. CPUs use HBM; GPUs use DDR

### Q18. What is the basic building block of an NVIDIA GPU that contains CUDA cores, Tensor Cores, registers, and shared memory?

- A. Streaming Multiprocessor (SM)
- B. NVSwitch
- C. Baseboard management controller
- D. Memory controller hub

### Q19. Why do GPUs need fewer large caches per core than CPUs?

- A. GPUs do not access memory
- B. GPUs only run integer operations
- C. GPUs store all data in registers
- D. GPUs hide memory latency by switching between many parallel threads

### Q20. How many ConnectX-7 400 Gb/s adapters does a DGX H100 dedicate to the compute fabric?

- A. 2
- B. 4
- C. 8
- D. 16

### Q21. Which resource is LEAST likely to be the main requirement when choosing hardware for classic machine learning (e.g., XGBoost) on a medium dataset with RAPIDS?

- A. GPU memory to hold the dataset
- B. Multi-node InfiniBand fabric with 400 Gb/s per GPU
- C. A GPU supported by RAPIDS
- D. Enough system memory for data loading

### Q22. An inference service experiences 10x more user traffic. What is the usual scaling approach?

- A. Scale up to a single larger GPU only
- B. Scale out by adding more inference replicas behind a load balancer
- C. Increase training epochs
- D. Disable dynamic batching

### Q23. Adding GPUs to a training job gives little speedup. The compute fabric is 3:1 oversubscribed. What is the most likely cause?

- A. Network bottleneck during gradient synchronization
- B. Too much GPU memory
- C. The model is too small for MIG
- D. The BMC firmware is old

### Q24. Which PUE value indicates the MOST energy-efficient data center?

- A. 2.0
- B. 1.6
- C. 1.4
- D. 1.1

### Q25. What does a 2N power design provide?

- A. Half the required capacity
- B. Exactly the required capacity with no spare
- C. Two fully independent power paths, each able to carry the full load
- D. One spare component

### Q26. Which factor favors on-premises AI infrastructure over cloud?

- A. Unpredictable, short-term demand
- B. Constant high utilization for years combined with strict data residency rules
- C. Need to start within one hour
- D. No in-house operations staff

### Q27. Which cost is specific to cloud environments and often surprises teams moving large datasets?

- A. Data egress fees
- B. Floor load rating
- C. Generator fuel
- D. Rack PDUs

### Q28. Which network connects to the BMCs of the servers?

- A. Compute fabric
- B. Storage fabric
- C. Spectrum-X fabric
- D. Out-of-band management network

### Q29. What is the role of login nodes in an AI cluster?

- A. Run the largest training jobs
- B. Act as InfiniBand switches
- C. Provide user access for editing code and submitting jobs, not heavy compute
- D. Host the BMC

### Q30. Which facility factor is often missed when planning dense GPU racks?

- A. Paint color
- B. Floor load (weight) rating and rack depth
- C. Parking spaces
- D. Wi-Fi coverage

### Q31. What should fill unused rack spaces in an air-cooled rack?

- A. Blanking panels
- B. Cardboard
- C. Nothing
- D. Extra cables

### Q32. Why is a lossless network important for distributed training?

- A. It reduces GPU power
- B. It increases storage capacity
- C. It allows longer cables
- D. Dropped packets cause retransmissions and tail latency that slow every synchronized GPU

### Q33. What oversubscription ratio is recommended for a GPU compute fabric used for large training jobs?

- A. 4:1
- B. 3:1
- C. 1:1 (non-blocking)
- D. 10:1

### Q34. How does InfiniBand avoid dropping packets under normal operation?

- A. TCP retransmission
- B. Credit-based link-level flow control
- C. Random early detection
- D. Larger MTU only

### Q35. Which InfiniBand speed generation provides 400 Gb/s per port?

- A. NDR
- B. HDR
- C. EDR
- D. FDR

### Q36. What is the role of NVSwitch in a DGX system?

- A. Connect the BMC
- B. Connect storage
- C. Convert Ethernet to InfiniBand
- D. Connect all GPUs so every GPU can talk to every other GPU at full NVLink bandwidth

### Q37. An organization runs a multi-tenant AI cloud and wants to stay on Ethernet. Which inter-node fabric fits best?

- A. NVLink-C2C
- B. PCIe switches
- C. NVIDIA Spectrum-X Ethernet
- D. 1 GbE copper

### Q38. Which SDK is used to develop applications for NVIDIA BlueField DPUs?

- A. CUDA
- B. DOCA
- C. NCCL
- D. cuDNN

### Q39. A cloud provider wants to offer bare-metal servers to tenants but keep control of networking and storage virtualization. What helps most?

- A. BlueField DPUs
- B. More CPU cores
- C. Time-slicing
- D. Larger hard disks

### Q40. Which modern standard provides a RESTful (JSON over HTTPS) API for server hardware management through the BMC?

- A. SNMPv1
- B. Redfish
- C. FTP
- D. SMTP

### Q41. A multi-node job fails only on certain nodes. Investigation shows different GPU driver versions across nodes. What is the best long-term fix?

- A. Manage nodes from a single golden image and roll updates consistently with a cluster manager
- B. Install drivers by hand on each node when jobs fail
- C. Use only one node
- D. Disable monitoring

### Q42. Which management network should carry IPMI/Redfish traffic to server BMCs?

- A. The GPU compute fabric
- B. The storage fabric
- C. NVLink
- D. A separate out-of-band management network

### Q43. What does the NVIDIA GPU Operator do in a Kubernetes cluster?

- A. It trains models automatically
- B. It replaces the Kubernetes scheduler
- C. It automates deployment of the GPU driver, container toolkit, device plugin, GPU feature discovery, DCGM exporter, and MIG manager
- D. It manages InfiniBand switches

### Q44. Which NVIDIA product adds team quotas, fair-share, and fractional GPU allocation on top of Kubernetes to raise GPU utilization?

- A. NVIDIA DOCA
- B. NVIDIA Run:ai
- C. NVIDIA Clara
- D. NVIDIA Jetson

### Q45. Which GPU Operator component labels nodes with GPU model, memory, and MIG capabilities?

- A. GPU Feature Discovery
- B. DCGM Exporter
- C. Node Problem Detector
- D. CoreDNS

### Q46. A GPU shows 100% 'GPU utilization' in nvidia-smi, but training is slower than expected. Which metric gives a better view of how much of the GPU is actually busy?

- A. Fan speed
- B. PCIe link width
- C. Driver version
- D. SM activity (DCGM_FI_PROF_SM_ACTIVE)

### Q47. What is the difference between single-bit (SBE) and double-bit (DBE) ECC errors?

- A. SBEs crash the application; DBEs are harmless
- B. Both are always corrected
- C. SBEs are corrected by ECC; DBEs are uncorrectable and can crash applications
- D. Neither affects GPU memory

### Q48. GPU utilization is low while CPU usage is near 100% during training. What is the most likely bottleneck?

- A. NVLink bandwidth
- B. The data loading and preprocessing pipeline
- C. GPU memory capacity
- D. BMC firmware

### Q49. Two different customers must share one H100 with guaranteed memory, cache, and compute. Which method fits best?

- A. MIG
- B. Time-slicing
- C. CUDA MPS
- D. Running both in one container

### Q50. Which consideration argues AGAINST partitioning GPUs for a workload?

- A. Many small inference models
- B. Notebook users with light workloads
- C. Need for tenant isolation
- D. A large model training job that needs full GPUs and fast NVLink between them

---

## Answer key

<details><summary>Show answers (only after you finish)</summary>

| Q | Answer | Topic | Why |
|---|---|---|---|
| 1 | **A** | 1.1 | Triton is a multi-framework inference server with dynamic batching and HTTP/gRPC APIs. |
| 2 | **A** | 1.1 | Containers carry CUDA libraries and frameworks; the host provides the kernel driver, exposed to containers by the NVIDIA Container Toolkit. |
| 3 | **D** | 1.2 | Inference runs the forward pass with fixed weights; latency, throughput, and cost per request are the key metrics. |
| 4 | **C** | 1.2 | Lower precision (FP16/FP8/INT8/FP4) reduces memory and increases throughput, usually with small accuracy loss. |
| 5 | **B** | 1.2 | FP16 uses 2 bytes per parameter: 7B x 2 = 14 GB (plus KV cache and runtime overhead). |
| 6 | **A** | 1.3 | Clustering without labels is unsupervised learning. |
| 7 | **D** | 1.3 | The labels (next tokens) come from the data itself: self-supervised learning. |
| 8 | **C** | 1.4 | Cloud lowered the entry barrier by providing on-demand GPU capacity. |
| 9 | **B** | 1.5 | Merlin is NVIDIA's framework for recommender systems. |
| 10 | **A** | 1.5 | RAG retrieves relevant documents and adds them to the prompt. |
| 11 | **D** | 1.5 | Clara (with MONAI) is NVIDIA's healthcare and medical imaging platform. |
| 12 | **C** | 1.6 | Hopper (H100) introduced the Transformer Engine with FP8. |
| 13 | **B** | 1.6 | GB200 NVL72 is a liquid-cooled rack with 72 GPUs in one NVLink domain. |
| 14 | **A** | 1.6 | Jetson modules provide embedded edge AI computing. |
| 15 | **D** | 1.7 | RAPIDS includes cuDF (DataFrames) and cuML (machine learning). |
| 16 | **C** | 1.7 | MLOps adds data/model versioning, model evaluation, and drift monitoring. |
| 17 | **B** | 1.8 | CPUs: few powerful cores, large caches. GPUs: thousands of simpler cores, high throughput. |
| 18 | **A** | 1.8 | The SM is the GPU's core processing block. |
| 19 | **D** | 1.8 | GPU throughput design uses massive multithreading to hide latency. |
| 20 | **C** | 2.1 | Eight single-port ConnectX-7 adapters: one per GPU (1:1 GPU-to-NIC ratio). |
| 21 | **B** | 2.1 | Such workloads usually run on one or a few GPUs; a multi-node fabric is not needed. |
| 22 | **B** | 2.2 | Inference scales out with replicas and autoscaling. |
| 23 | **A** | 2.2 | Oversubscription limits all-reduce bandwidth, so GPUs wait. |
| 24 | **D** | 2.3 | Lower is better; 1.0 is the theoretical ideal. |
| 25 | **C** | 2.3 | 2N = two complete, independent systems (A and B feeds). N+1 = one spare component. |
| 26 | **B** | 2.4 | Steady utilization lowers on-prem TCO; data residency may require on-prem. |
| 27 | **A** | 2.4 | Clouds charge for data transferred out. |
| 28 | **D** | 2.5 | BMCs use a separate out-of-band network. |
| 29 | **C** | 2.5 | Users connect to login nodes and submit jobs to the scheduler. |
| 30 | **B** | 2.6 | DGX systems are heavy and deep; floors and racks must support them. |
| 31 | **A** | 2.6 | Blanking panels stop hot air from recirculating to the front. |
| 32 | **D** | 2.7 | Synchronous training runs at the speed of the slowest participant. |
| 33 | **C** | 2.7 | Training fabrics are designed non-blocking. |
| 34 | **B** | 2.8 | Senders transmit only when the receiver advertises buffer credits. |
| 35 | **A** | 2.8 | EDR 100, HDR 200, NDR 400, XDR 800 Gb/s. |
| 36 | **D** | 2.9 | NVSwitch provides an all-to-all NVLink fabric. |
| 37 | **C** | 2.9 | Spectrum-X is NVIDIA's AI Ethernet fabric for multi-tenant clouds. |
| 38 | **B** | 2.10 | DOCA is the DPU software framework. |
| 39 | **A** | 2.10 | The DPU runs provider-controlled infrastructure services separately from the tenant's host. |
| 40 | **B** | 3.1 | Redfish is the modern REST API; IPMI is the older protocol. |
| 41 | **A** | 3.1 | Configuration consistency prevents version drift. |
| 42 | **D** | 3.1 | BMC traffic stays on the OOB network, isolated from production traffic. |
| 43 | **C** | 3.2 | The GPU Operator manages all software needed to use GPUs in Kubernetes. |
| 44 | **B** | 3.2 | Run:ai is a Kubernetes-based GPU orchestration platform. |
| 45 | **A** | 3.2 | GPU Feature Discovery (GFD) generates node labels. |
| 46 | **D** | 3.3 | GPU utilization only measures the time a kernel runs; SM activity measures how many SMs are busy. |
| 47 | **C** | 3.3 | SBE = corrected (watch trend); DBE = uncorrectable (XID 48). |
| 48 | **B** | 3.3 | The GPUs wait for data; use more workers, DALI, or faster storage. |
| 49 | **A** | 3.4 | MIG provides hardware-partitioned, isolated GPU instances. |
| 50 | **D** | 3.4 | Large training needs whole GPUs and nodes; partitioning reduces available compute per job. |

</details>

**Score guide:** 40+/50 (80%) = ready. 35–39 = review weak topics. Below 35 = repeat the study plan week for weak domains.
