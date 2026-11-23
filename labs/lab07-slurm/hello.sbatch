#!/bin/bash
#SBATCH --job-name=hello
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:02:00
#SBATCH --output=hello-%j.out
srun bash -c 'echo "task $SLURM_PROCID of $SLURM_NTASKS on $(hostname)"; sleep 20'
