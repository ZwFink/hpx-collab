#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH -p buran
#SBATCH -w "buran01"
#SBATCH --time=00:50:00
#SBATCH --job-name=openmp_1node_%j
#SBATCH --output=openmp-1node-%j.txt
#SBATCH --error=error-%j.txt

module purge

module load gcc/11.2.0
module load boost/1.78.0-release
module load cmake/3.22.0
module load hwloc/2.6.0
module load openmpi/4.1.2


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PROC_BIND=true
export OMP_PLACES=cores

echo "This script is used to run OpenMP task bench 1 buran nodes, width 48 fixed width, from 2(6) to 2(24) "
date

for rn in {1..5..1}
do
	for i in {6..24..3}
	do
        	it=$((2 ** $i))
        	echo "using iter: "
        	echo ${it}
        	cd /work/nanmiao/taskbench/src/task-bench/openmp/
        	srun  main -type stencil_1d  -width 48 -steps 1000 -kernel compute_bound -iter ${it} -worker 48
        	echo "done iter =====================================  "

	done
done

echo "complete all runs"
date


~
