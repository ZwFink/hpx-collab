#!/bin/bash
module load openmpi
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_8node_nonsmp.sh 1 2022-02-07_stencil/8node_odf1.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_8node_nonsmp.sh 4 2022-02-07_stencil/8node_odf4.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_8node_nonsmp.sh 8 2022-02-07_stencil/8node_odf8.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_8node_nonsmp.sh 16 2022-02-07_stencil/8node_odf16.txt
