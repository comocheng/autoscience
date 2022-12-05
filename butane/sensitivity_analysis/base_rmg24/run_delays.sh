#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=west,express,short
#SBATCH --array=0-1000%20


offset=0
model_num=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $offset)))
python get_delay.py $model_num > "results/ignition_delays/delay_$model_num.txt"


offset=1000
model_num=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $offset)))
python get_delay.py $model_num > "results/ignition_delays/delay_$model_num.txt"

