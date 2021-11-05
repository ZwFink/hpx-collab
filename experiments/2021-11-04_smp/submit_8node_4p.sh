#!/bin/bash
#SBATCH --nodes=8
#SBATCH --tasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --partition=buran
#SBATCH --time=1:00:00
#SBATCH --exclusive

nnodes=8
ppn=4
width=$((384-(nnodes*ppn)))
# note: auto-provision only works with one OS Process per node
python3 $HOME/hpx-collab/scripts/run.py --basedir $BASEDIR --ntasks 1000 --iter $((1<<6)) $((1<<27)) 8 --output_file "$1" --width $width --steps 1000 --run_args "+setcpuaffinity" --type stencil_1d --trials 3 --run_args "++ppn 11"
