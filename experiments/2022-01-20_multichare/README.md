These experiments were performed on 2022-01-20 to determine the effect of having multiple vertices per PE on performance of Task-Bench. We considered three different versions: 
- Charm++ built with the UCX backed in SMP mode
  Built via: ```./build charm++ ucx-linux-x86_64 --with-production -j10 --force slurmpmi smp --basedir=/opt/apps/ucx/1.11.2```
- Charm++ built with the UCX backed in non-SMP mode
  Built via: ```./build charm++ ucx-linux-x86_64 --with-production -j10 --force slurmpmi --basedir=/opt/apps/ucx/1.11.2```
- MPI given from the Rostam system via ```module load openmpi```

- Charm++ experiments performed on commit 001844861092d357a96dc9b28d7ee99eb8027db2
- MPI experiments performed on OpenMPI v4.1.2


These are the exact experiments performed on 2022-01-19, but were redone because of the high variability in the measurements taken. Thus, these experiments were performed with 6 iterations instead of 3
