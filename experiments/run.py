import sh
import click
import random
import time

@click.command()
@click.option('--basedir', type=str)
@click.option('--ntasks', type=int)
@click.option('--iter', nargs=3, type=int)
@click.option('--output', type=click.File('w'))
@click.option('--width', type=int)
@click.option('--steps', type=int, help="Number of steps, start, stop, step. Increments in "
              "multiples of step."
              )
@click.option('--type', type=str)
@click.option('--trials', type=int, default=5)
@click.option('--charm_args', multiple=True, type=str)
def main(**kwargs):
    start, stop, step = kwargs['iter']
    iter_counts = [start]

    while iter_counts[-1] < stop:
        iter_counts.append(iter_counts[-1]*step)

    outf = kwargs['output']
    base_cmd = get_charmrun_command(kwargs['basedir'])
    full_cmd = base_cmd.bake('-kernel', 'compute_bound',
                            '-width', kwargs['width'],
                            '-steps', kwargs['steps'],
                            '-type', kwargs['type'],
                            ' '.join(kwargs['charm_args'])
                  )
    for tnum in range(kwargs['trials']):
        tstart = time.time()
        random.shuffle(iter_counts)
        for niter in iter_counts:
            run_cmd = full_cmd.bake('-iter', niter)
            print('#'+str(run_cmd), file=outf)
            outf.flush()
            run_cmd(_out=outf)
        elapsed = time.time()-tstart
        print(f"Trial {tnum} took {elapsed}s.")

def get_charmrun_command(basedir):
    import os
    # todo: update for SMP compatibility
    ntasks = os.getenv('SLURM_NTASKS')
    return sh.srun.bake('-n', 48, '-c', 1,
                        basedir + '/benchmark'
                        )

if __name__ == '__main__':
    main()
