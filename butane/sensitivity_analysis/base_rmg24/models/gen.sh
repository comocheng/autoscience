#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --partition=west,express,short
#SBATCH --array=0-500%20


offset=1800

model_num=$(($SLURM_ARRAY_TASK_ID + $offset))

python gen.py $model_num

