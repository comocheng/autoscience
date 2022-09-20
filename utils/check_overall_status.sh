#!/bin/bash
#SBATCH --job-name=overall_status
#SBATCH --partition=express,short,west
#SBATCH --time=00:00:01

# script to run check on status of shell scripts
python /work/westgroup/harris.se/autoscience/autoscience/utils/check_overall_status.py $1 



