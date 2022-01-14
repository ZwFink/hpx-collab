#!/bin/bash
#SBATCH --nodes=1
#SBATCH --tasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --partition=buran
#SBATCH --time=3:05:00
#SBATCH --exclusive

width=48
python3 $HOME/hpx-collab/scripts/run.py --basedir $BASEDIR --ntasks 1000 --iter $((1<<6)) $((1<<27)) 8 --output_file "$1" --width $width --steps 1000 --type stencil_1d --trials 3 --run_args "+setcpuaffinity"
