#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --partition=short,west
#SBATCH --array=0-1000%50


offset=0
padded_model_num=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $offset)))
python run_flames.py "chem_$padded_model_num.cti"

offset=1000
padded_model_num=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $offset)))
python run_flames.py "chem_$padded_model_num.cti"

