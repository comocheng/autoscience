#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --partition=west,express,short
#SBATCH --array=0-110%50


offset=0

model_num=$(($SLURM_ARRAY_TASK_ID + $offset))

python gen.py $model_num

