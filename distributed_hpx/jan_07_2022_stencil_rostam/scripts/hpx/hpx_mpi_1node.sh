#!/bin/bash
##SBATCH --nodes=1
##SBATCH --ntasks-per-node=2
##SBATCH --ntasks=2
##SBATCH --cpus-per-task=24
#SBATCH -p buran
#SBATCH -w "buran01"
#SBATCH --time=00:10:00
#SBATCH --job-name=hpx-plainmpi-join-1node-%j
#SBATCH --output=hpx-plainmpi-join-1node-%j.txt
#SBATCH --error=error-%j.txt

#module purge
module load gcc/11.2.0
module load boost/1.78.0-release
module load cmake/3.22.0
module load hwloc/2.6.0
module load pmix/4.1.0 
module load openmpi/4.1.2

echo "This script is used to run distributed HPX (plain MPI + fork-join-executor) task bench 1 buran nodes, width 48 fixed width, from 2(6) to 2(27) "
date

for rn in {1..5..1}
do
	for i in {6..24..3}
	do
        	it=$((2 ** $i))
		echo "using iter: "
        	echo ${it}
        	cd /work/nanmiao/taskbench/src/task-bench/hpx/build_Release/bin/
        	srun -N 1 -n 1 -c 48 mpi_executor -type stencil_1d  -width 48 -steps 1000 -kernel compute_bound -iter ${it} -hpx:threads=48
        	echo "done iter =====================================  "
        	date
	done
done
echo "complete all runs"
date


