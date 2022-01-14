#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=48
#SBATCH -p buran
#SBATCH --time=00:10:00
#SBATCH --job-name=hpx-plainmpi-join-2node-%j
#SBATCH --output=hpx-plainmpi-join-2node-%j.txt
#SBATCH --error=error-%j.txt

module purge
module load gcc/10.2.0
module load boost/1.75.0-release
module load cmake/3.19.5
module load hwloc/2.4.1
module load openmpi/4.0.5

echo "This script is used to run distributed HPX (plain MPI + fork-join-executor) task bench 2 buran nodes, width 96 fixed width, from 2(6) to 2(24) "
date

iter_list=(64, 512, 4096, 32768, 262144, 2097152, 16777216)

for it in "${iter_list[@]}"
do
        echo "using iter: "
        echo ${it}
        cd /work/nanmiao/taskbench/src/task-bench/hpx/build_Release/bin/
        srun mpi_executor -type stencil_1d  -width 96 -steps 1000 -kernel compute_bound -iter ${it}
        echo "done iter =====================================  "
        date
done
date

