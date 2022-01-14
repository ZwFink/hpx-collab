#!/bin/bash
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=48
#SBATCH -p buran
#SBATCH -w "buran[08-15]"
#SBATCH --time=32:00:00
#SBATCH --job-name=mpi_openmp_8node_%j
#SBATCH --output=mpi-openmp-8node-%j.txt
#SBATCH --error=error-%j.txt

module purge

module load gcc/11.2.0
module load boost/1.78.0-release
module load cmake/3.22.0
module load hwloc/2.6.0
module load openmpi/4.1.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export export OMP_PLACES=cores
export OMP_PROC_BIND=true

echo "This script is used to run distributed MPI+OpenMP task bench 8 buran nodes, width 384 fixed width, from 2(6) to 2(24) "
date

for rn in {1..5..1}
do
	for i in {6..24..3}
	do
        	it=$((2 ** $i))
        	echo "using iter: "
        	echo ${it}
        	cd /work/nanmiao/taskbench/src/task-bench/mpi_openmp/
        	srun forall -type stencil_1d  -width 384 -steps 1000 -kernel compute_bound -iter ${it} 
        	echo "done iter =====================================  "

	done
done

echo "complete all runs"

date

