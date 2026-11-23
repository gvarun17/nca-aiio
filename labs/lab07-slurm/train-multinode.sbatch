#!/bin/bash
# Multi-node GPU training on a DGX cluster (Slurm + Pyxis/Enroot + NGC container)
#SBATCH --job-name=llm-pretrain
#SBATCH --partition=batch
#SBATCH --nodes=4
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=8            # one rank per GPU
#SBATCH --cpus-per-task=14
#SBATCH --exclusive                    # whole nodes, no sharing
#SBATCH --time=48:00:00
#SBATCH --output=logs/%x-%j.out

export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n1)
export MASTER_PORT=29500
export NCCL_IB_HCA=mlx5                # use the InfiniBand ConnectX adapters
export NCCL_DEBUG=WARN

srun --container-image=nvcr.io#nvidia/pytorch:24.10-py3 \
     --container-mounts=/lustre/datasets:/data,/lustre/checkpoints:/ckpt \
     python train.py --data /data/corpus --checkpoint-dir /ckpt --save-every 1000
