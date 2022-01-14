These experiments were done to investigate whether Charm++ built with the MPI backend performs better than Charm++ built with the UCX backend, as was suggested could be the case by Simeng

OpenMPI as obtained by ```module load openmpi``` was used as the MPI implementation.
Charm++ was build in the following ways:
```bash
# SMP-mode with MPI backend
 ./build charm++ mpi-linux-x86_64 smp --with-production -j10 
# Non-SMP mode with MPI backend
 ./build charm++ mpi-linux-x86_64 --with-production -j10 
```
