#!/bin/bash
#SBATCH --time=1-00:00:00
#SBATCH --partition=short,west
#SBATCH --array=0-300%20


offset=1800
model_num=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $offset)))
python get_flame_speed.py $model_num

