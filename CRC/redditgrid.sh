#!/usr/bin/env bash

#SBATCH --job-name=redditgridsearch
#SBATCH --output=gridsearch.out
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --partition=smp
#SBATCH --cluster=smp
#SBATCH --mem 32000
#SBATCH --time 10:00:00

module load python/3.7.0

python redditgrid.py

crc-job-stats.py
