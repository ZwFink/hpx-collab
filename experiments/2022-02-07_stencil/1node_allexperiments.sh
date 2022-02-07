#!/bin/bash

BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_1node_nonsmp.sh 1 2022-02-07_stencil/1node_odf1.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_1node_nonsmp.sh 4 2022-02-07_stencil/1node_odf4.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_1node_nonsmp.sh 8 2022-02-07_stencil/1node_odf8.txt
BASEDIR=$HOME/task-bench/charm++/benchmark sbatch submit_1node_nonsmp.sh 16 2022-02-07_stencil/1node_odf16.txt
