These experiments were performed on 2022-02-07 in order to assess the performance of Charm++ in the Task-Bench benchmark for the stencil1d pattern. ODF factors (number of vertices per chare, with one chare per PE) of 1, 4, 8, 16 were used. Following the fine-grained performance analysis of earlier, Charm++ was built with the following command:

```bash
./build AMPI-only ucx-linux-x86_64 --enable-shmem --with-prio-type=char --with-production -j10 --force slurmpmi --basedir=/opt/apps/ucx/1.11.2 -DCMK_NO_MSG_PRIOS=1 -DCSD_NO_IDLE_TRACING=1 -DCSD_NO_PERIODIC=1 -DCSD_NO_SCHEDLOOP=1
```
