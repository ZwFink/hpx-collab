import sh
import click
import random
import time

@click.command()
@click.option('--basedir', type=str)
@click.option('--ntasks', type=int)
@click.option('--iter', nargs=3, type=int)
@click.option('--output_file', type=click.File('w'))
@click.option('--width', type=int)
@click.option('--steps', type=int, help="Number of steps, start, stop, step. Increments in "
              "multiples of step."
              )
@click.option('--type', type=str)
@click.option('--trials', type=int, default=5)
@click.option('--run_args', multiple=True, type=str)
@click.option('--run_args_first', is_flag=True)
@click.option('--kernel', type=str, default="compute_bound", help="Task Bench kernel type to run")
@click.option('--ngraphs', type=int, default=1, help="Number of concurrent "
              "graphs to execute. "
              "Currently, only supports executing the same graph n thimes."
              )
@click.option('--radix', type=int, default=1)
# TODO: What is a good default for output?
@click.option('--output', type=int, default=1)
def main(**kwargs):
    start, stop, step = kwargs['iter']
    iter_counts = [start]

    while iter_counts[-1] < stop:
        iter_counts.append(iter_counts[-1]*step)

    outf = kwargs['output_file']
    run_args = ' '.join(kwargs['run_args'])
    base_cmd = get_run_cmd(kwargs['basedir'])
    single_graph_cmd = ('-kernel', kwargs['kernel'],
                        '-width', kwargs['width'],
                        '-steps', kwargs['steps'],
                        '-type', kwargs['type'],
                        '-radix', kwargs['radix'],
                        '-output', kwargs['output']
                        )
    base_graph_cmd = []
    if kwargs['run_args_first']:
        base_graph_cmd.append(run_args)
    base_graph_cmd += single_graph_cmd

    for i in range(1, kwargs['ngraphs']):
        base_graph_cmd.append('-and')
        base_graph_cmd += single_graph_cmd

    if not kwargs['run_args_first']:
        base_graph_cmd.append(run_args)

    full_cmd = base_cmd.bake(*base_graph_cmd)
    for tnum in range(kwargs['trials']):
        tstart = time.time()
        random.shuffle(iter_counts)
        for niter in iter_counts:
            run_cmd = full_cmd.bake('-iter', niter)
            print('#'+str(run_cmd), file=outf)
            #outf.flush()
            #run_cmd(_out=outf)
        elapsed = time.time()-tstart
        print(f"Trial {tnum} took {elapsed}s.")

def get_run_cmd(basedir):
    import os
    # todo: update for SMP compatibility
    ntasks = os.getenv('SLURM_NTASKS')
    return sh.srun.bake('-n', ntasks, '-c', 1,
                        '--mpi=pmi2',
                        basedir
                        )

if __name__ == '__main__':
    main()
