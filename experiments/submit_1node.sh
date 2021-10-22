#!/bin/bash
#SBATCH --nodes=1
#SBATCH --tasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --partition=buran
#SBATCH --time=30:00
#SBATCH --exclusive
#SBATCH -o nan_parameters.txt
nnodes=1
./charmrun +p $((nnodes*48)) ./benchmark -kernel compute_bound -iter $((2 ** 24)) -width 48 -steps 1000 -type stencil_1d +setcpuaffinity
