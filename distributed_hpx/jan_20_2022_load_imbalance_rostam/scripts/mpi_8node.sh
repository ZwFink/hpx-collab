#!/bin/bash
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=48
#SBATCH --ntasks=384
#SBATCH --cpus-per-task=1
#SBATCH -p buran
#SBATCH -w "buran[08-15]"
#SBATCH --time=01:10:00
#SBATCH --job-name=mpi_non_8node_%j
#SBATCH --output=mpi-non-8node-%j.txt
#SBATCH --error=error-%j.txt


module purge

module load gcc/11.2.0
module load boost/1.78.0-release
module load cmake/3.22.0
module load hwloc/2.6.0
module load openmpi/4.1.2


echo "This script is used to run distributed MPI Nonblock task bench 8 buran nodes, width 384 fixed width, from 2(6) to 2(24) load imbalance nearest pattern, 5 dependeces/task"
date

for rn in {1..5..1}
do
	for i in {6..24..3}
	do
        	it=$((2 ** $i))
        	echo "using iter: "
        	echo ${it}
        	cd /work/nanmiao/taskbench/src/task-bench/mpi/
        	srun nonblock -type nearest -radix 5  -width 384 -steps 1000 -kernel  load_imbalance -iter ${it} -imbalance 0.1
        	echo "done iter =====================================  "

	done
done

echo "complete all runs"
date



