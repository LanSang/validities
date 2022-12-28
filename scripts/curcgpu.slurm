#!/bin/bash

#SBATCH --partition=ami100
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --gres=gpu

module load anaconda

module load cuda/11.3
conda create -name gpu
conda activate gpu
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch
python tmp.py
