#!/bin/bash
# Hyperparameter sweep: 8 independent 1-GPU jobs (job array)
#SBATCH --job-name=sweep
#SBATCH --array=0-7
#SBATCH --gpus=1
#SBATCH --time=02:00:00
LRS=(1e-3 5e-4 3e-4 1e-4 5e-5 3e-5 1e-5 5e-6)
srun python train.py --lr ${LRS[$SLURM_ARRAY_TASK_ID]}
