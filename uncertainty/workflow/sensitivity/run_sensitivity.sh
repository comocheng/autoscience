#!/bin/bash
#SBATCH --partition=short,west
#SBATCH --time=1-00:00:00
#SBATCH --ntasks=32

python "/work/westgroup/harris.se/autoscience/autoscience/uncertainty/workflow/sensitivity/sensitivity.py"
