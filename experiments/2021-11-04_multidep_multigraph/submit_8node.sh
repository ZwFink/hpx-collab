#!/bin/bash
#SBATCH --nodes=8
#SBATCH --tasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --partition=buran
#SBATCH --time=1:00:00
#SBATCH --exclusive

width=384
python3 run.py --basedir $BASEDIR --ntasks 1000 --iter $((1<<6)) $((1<<27)) 8 --output "$1" --width $width --steps 1000 --charm_args "+setcpuaffinity" --type stencil_1d --trials 3
