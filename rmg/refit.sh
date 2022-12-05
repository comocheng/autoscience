#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --mem=20Gb
#SBATCH --cpus-per-task=16


python refit_tree.py


