#!/bin/bash
#SBATCH --partition=express,short,west
#SBATCH --time=00:20:00

python /work/westgroup/harris.se/autoscience/autoscience/butane/dft/scripts/run_one_arkane.py $1

