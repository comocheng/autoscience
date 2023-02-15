#!/bin/bash
#SBATCH --job-name=check_vibes
#SBATCH --time=00:10:00
#SBATCH --array=0-1000%50
#SBATCH --partition=express,short,west

#BASE=0
BASE=1000
REACTION_INDEX=$(( $BASE + $SLURM_ARRAY_TASK_ID ))

python /work/westgroup/harris.se/autoscience/autoscience/verification/check_vibes.py $REACTION_INDEX

