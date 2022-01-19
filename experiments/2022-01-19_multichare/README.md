These experiments were performed on 2022-01-19 to determine the effect of having multiple vertices per PE on performance of Task-Bench. We considered three different versions: 
- Charm++ built with the UCX backed in SMP mode
  Built via: ```./build charm++ ucx-linux-x86_64 --with-production -j10 --force slurmpmi smp --basedir=/opt/apps/ucx/1.11.2```
- Charm++ built with the UCX backed in non-SMP mode
  Built via: ```./build charm++ ucx-linux-x86_64 --with-production -j10 --force slurmpmi --basedir=/opt/apps/ucx/1.11.2```
- MPI given from the Rostam system via ```module load openmpi```
