#!/bin/bash
#SBATCH --nodes=8
#SBATCH --tasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --partition=buran
#SBATCH --time=9:00:00
#SBATCH --exclusive

nnodes=8
ppn=1
odf="$1"
width=$((odf*384))
# note: auto-provision only works with one OS Process per node
python3 $HOME/hpx-collab/scripts/run.py --basedir $BASEDIR --ntasks 1000 --iter $((1<<6)) $((1<<27)) 8 --output_file "$2" --width $width --steps 1000 --type stencil_1d --trials 6 --run_args "+pemap L0-47"


#  --basedir TEXT
#  --ntasks INTEGER
#  --iter INTEGER...
#  --output_file FILENAME
#  --width INTEGER
#  --steps INTEGER         Number of steps, start, stop, step. Increments in
#                          multiples of step.
#  --type TEXT
#  --trials INTEGER
#  --run_args TEXT
#  --run_args_first
#  --kernel TEXT           Task Bench kernel type to run
#  --ngraphs INTEGER       Number of concurrent graphs to execute. Currently,
#                          only supports executing the same graph n thimes.
#  --radix INTEGER
#  --output INTEGER

