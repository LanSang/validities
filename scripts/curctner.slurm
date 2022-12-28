#!/bin/bash

#SBATCH --partition=ami100
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --mem=8G
#SBATCH --gres=gpu

module load anaconda

conda env remove -n causaldsr
conda env create -f config/causaldsr.yml
conda activate causaldsr
python scripts/runtner.py
