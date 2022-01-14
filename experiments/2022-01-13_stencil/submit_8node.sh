#!/bin/bash
#SBATCH --nodes=8
#SBATCH --tasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --partition=buran
#SBATCH --time=1:30:00
#SBATCH --exclusive

# Non-smp mode
width=384
# note: auto-provision only works with one OS Process per node
python3 $HOME/hpx-collab/scripts/run.py --basedir $BASEDIR --ntasks 1000 --iter $((1<<6)) $((1<<27)) 8 --output_file "$1" --width $width --steps 1000 --type stencil_1d --trials 3 --run_args "+pemap L0-47"
