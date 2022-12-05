#!/bin/bash
#SBATCH --partition=express,short,west
#SBATCH --time=00:00:30
#SBATCH --array=0-10%5

offset=0
model_number=$((offset + $SLURM_ARRAY_TASK_ID))

python "/work/westgroup/harris.se/autoscience/autoscience/uncertainty/workflow/sensitivity/generate_cti.py" $model_number
