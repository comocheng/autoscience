#!/bin/bash
#SBATCH --ntasks=16
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --constraint=cascadelake


python run_flame_speeds.py $1

