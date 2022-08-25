#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --array=0-1000%40


SLURM_TASK_ID_OFFSET=0
# SLURM_TASK_ID_OFFSET=1000
# SLURM_TASK_ID_OFFSET=2000
# SLURM_TASK_ID_OFFSET=3000
# SLURM_TASK_ID_OFFSET=4000

RUN_i=$(printf "%04.0f" $(($SLURM_ARRAY_TASK_ID + $SLURM_TASK_ID_OFFSET)))

cti2yaml "models/chem_${RUN_i}.cti"
