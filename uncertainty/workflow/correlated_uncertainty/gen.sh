#!/bin/bash
#SBATCH --time=00:01:00
#SBATCH --partition=west,short,express
#SBATCH --array=0-1000%50

offset=0
model_num=$(($SLURM_ARRAY_TASK_ID + $offset))
python gen.py $model_num

offset=1000
model_num=$(($SLURM_ARRAY_TASK_ID + $offset))
python gen.py $model_num

offset=2000
model_num=$(($SLURM_ARRAY_TASK_ID + $offset))
python gen.py $model_num

offset=3000
model_num=$(($SLURM_ARRAY_TASK_ID + $offset))
python gen.py $model_num

offset=4000
model_num=$(($SLURM_ARRAY_TASK_ID + $offset))
python gen.py $model_num
