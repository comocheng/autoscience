#!/bin/bash
#SBATCH --job-name=flame_speed
#SBATCH --nodes=1
#SBATCH --partition=short
#SBATCH --mem=20Gb
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=16


python /work/westgroup/harris.se/autoscience/autoscience/flame_speed/run_flame_speeds.py $1
 
