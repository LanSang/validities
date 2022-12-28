#!/bin/bash 

#SBATCH --partition=amilan
#SBATCH --job-name=conda
#SBATCH --time=14:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1

# module load slurm/summit to access summit scheduler

source /curc/sw/anaconda3/latest

module load conda

conda env create -f config/causaldsr.yml
