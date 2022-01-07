import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from os import listdir
from os.path import isfile, join

font = {'size'   : 12}
matplotlib.rc('font', **font)

def get_args():
    parser = argparse.ArgumentParser('python')

    parser.add_argument('-mpi_input_dir',
                        required=False,
                        default='/home/nanmiao/Documents/plot_hpx/Jan_2022_data/Jan_06/Jan_06_mpi_others/',
                        help='')
                        
    parser.add_argument('-hpx_input_dir',
                        required=False,
                        default='/home/nanmiao/Documents/plot_hpx/Jan_2022_data/Jan_06/Jan_06_hpx_distributed_jemalloc_hpx_local_tcmalloc/',
                        help='')
    

    parser.add_argument('-mpi_output_dir',
                        required=False,
                        default='/home/nanmiao/Documents/plot_hpx/Jan_2022_data/Jan_06/2022_0107_mpi_others_stencil_1d.csv',
                        help='')
    

    parser.add_argument('-hpx_output_dir',
                        required=False,
                        default='/home/nanmiao/Documents/plot_hpx/Jan_2022_data/Jan_06/2022_0107_hpx_stencil_1d.csv',
                        help='')

   
    return parser.parse_args()
##########################################################################

def parse_result(file_path, df, ncpu, framwork):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    temp = []
    for i, line in enumerate(lines):
        line = line.split(' ')
        if line[0] == 'Elapsed' and line[1] == 'Time':
            elapsed = float(line[2])
            temp.append(elapsed)
        elif line[0] == 'FLOP/s':
            flops = float(line[1])
            temp.append(flops)
        elif line[0] == "using" and line[1] == "iter:":
            iter = int(lines[i+1].strip(','))
            temp.append(iter)

        if len(temp) == 3:
            temp = [framwork, ncpu] + temp
            df.loc[len(df.index)] = temp
            temp = []
        
###############################################################################

def plot_err_band_all_1node(charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc, 
                            hpx_local_tcmalloc, openmp):
    dfs = pd.concat([charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc,  
                     hpx_local_tcmalloc, openmp], ignore_index = True)
    ax=sns.lineplot(x='iter',y='flops', data=dfs, sort=False, 
            #markers=['d','o','s','X', '<'],
            markers=True,
            style='framework',hue='framework',ci=99,
            dashes=True,
            linewidth=3, markersize=10)
    ax.set_xscale('log',base=2)
    ax.set_xlim(1<<6, 1<<24)
    ax.set_ylabel('FLOP/s')
    ax.set_xlabel('Problem Size (Iterations)')

    plt.title('Stencil Rostam 1 node')
    ax.legend(fontsize = 12, loc = 'lower right', fancybox = False, framealpha = 1,
              handlelength = 1.7, ncol = 1)
    plt.show()


###############################################################################

def plot_err_band_all_2_node(charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc):
    dfs = pd.concat([charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc], ignore_index = True)
    ax=sns.lineplot(x='iter',y='flops', data=dfs, sort=False, 
            #markers=['d','o','s','X', '<'],
            markers=True,
            style='framework',hue='framework',ci=99,
            dashes=True,
            linewidth=3, markersize=10)
    ax.set_xscale('log',base=2)
    ax.set_xlim(1<<6, 1<<24)
    ax.set_ylabel('FLOP/s')
    ax.set_xlabel('Problem Size (Iterations)')

    plt.title('Stencil Rostam 2 nodes')
    ax.legend(fontsize = 12, loc = 'lower right', fancybox = False, framealpha = 1,
              handlelength = 1.7, ncol = 1)
    plt.show()

###############################################################################

def plot_err_band_all_4_node(charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc):
    dfs = pd.concat([charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc], ignore_index = True)
    ax=sns.lineplot(x='iter',y='flops', data=dfs, sort=False, 
            #markers=['d','o','s','X', '<'],
            markers=True,
            style='framework',hue='framework',ci=99,
            dashes=True,
            linewidth=3, markersize=10)
    ax.set_xscale('log',base=2)
    ax.set_xlim(1<<6, 1<<24)
    ax.set_ylabel('FLOP/s')
    ax.set_xlabel('Problem Size (Iterations)')

    plt.title('Stencil Rostam 4 nodes')
    ax.legend(fontsize = 12, loc = 'lower right', fancybox = False, framealpha = 1,
              handlelength = 1.7, ncol = 1)
    plt.show()

###############################################################################

def plot_err_band_all_8_node(charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc):
    dfs = pd.concat([charm, mpi_non, mpi_bulk, mpi_openmp, hpx_jemalloc], ignore_index = True)
    ax=sns.lineplot(x='iter',y='flops', data=dfs, sort=False, 
            #markers=['d','o','s','X', '<'],
            markers=True,
            style='framework',hue='framework',ci=99,
            dashes=True,
            linewidth=3, markersize=10)
    ax.set_xscale('log',base=2)
    ax.set_xlim(1<<6, 1<<24)
    ax.set_ylabel('FLOP/s')
    ax.set_xlabel('Problem Size (Iterations)')

    plt.title('Stencil Rostam 8 nodes')
    ax.legend(fontsize = 12, loc = 'lower right', fancybox = False, framealpha = 1,
              handlelength = 1.7, ncol = 1)
    plt.show()


###############################################################################
    
if __name__ == '__main__':
    args = get_args()
    mpi_input_dir = args.mpi_input_dir
    mpi_output_dir = args.mpi_output_dir

    hpx_input_dir = args.hpx_input_dir
    hpx_output_dir = args.hpx_output_dir
###################################################################################
    # get charm++ data
    df_charm = pd.read_csv('/home/nanmiao/Documents/plot_hpx/2021-10-22_stencil_1d.csv')
    df_charm=df_charm.sort_values(by='NITER',ascending=False)
    df_charm['Framework'] = 'Charm++'
    df_charm.rename(columns={"NCPU": "ncpu", "NITER": "iter", "FLOPS": "flops", "Framework": "framework"}, inplace=True)
    charm_1node = df_charm[df_charm['ncpu'] == 48]
    charm_2node = df_charm[df_charm['ncpu'] == 96]
    charm_4node = df_charm[df_charm['ncpu'] == 192]
    charm_8node = df_charm[df_charm['ncpu'] == 384]
    charm_1node['framework'] = 'Charm++ 1 node'
    charm_2node['framework'] = 'Charm++ 2 node'
    charm_4node['framework'] = 'Charm++ 4 node'
    charm_8node['framework'] = 'Charm++ 8 node'

###################################################################################
    # read all mpi and hpx
    all_other_files = [f for f in listdir(mpi_input_dir) if isfile(join(mpi_input_dir, f))]
    all_hpx_files = [f for f in listdir(hpx_input_dir) if isfile(join(hpx_input_dir, f))]

###################################################################################
    # mpi, openmp, mpi_openmp
    df = pd.DataFrame(columns=['framework', 'ncpu', 'iter', 'elapsed', 'flops'])
    for f in sorted(all_other_files):
        f_split = f.split("-")
        n = len(f_split)
        idx = n - 2
        framework = f_split[0:idx]
        framework = "-".join(framework)
        ncpu = 48 * int(f_split[idx][0])
        
        parse_result(join(mpi_input_dir, f), df, ncpu, framework)
    df.to_csv(mpi_output_dir, index=False)
    
    mpi_nonblock_1node = df[(df['framework']== 'mpi-non') & (df['ncpu'] == 48 * 1) ]
    mpi_nonblock_2node = df[(df['framework']== 'mpi-non') & (df['ncpu'] == 48 * 2) ]
    mpi_nonblock_4node = df[(df['framework']== 'mpi-non') & (df['ncpu'] == 48 * 4) ]
    mpi_nonblock_8node = df[(df['framework']== 'mpi-non') & (df['ncpu'] == 48 * 8) ]
    mpi_nonblock_1node['framework'] = 'MPI nonblock 1 node'
    mpi_nonblock_2node['framework'] = 'MPI nonblock 2 nodes'
    mpi_nonblock_4node['framework'] = 'MPI nonblock 4 nodes'
    mpi_nonblock_8node['framework'] = 'MPI nonblock 8 nodes'

    mpi_bulk_1node = df[(df['framework']== 'mpi-bulk') & (df['ncpu'] == 48 * 1) ]
    mpi_bulk_2node = df[(df['framework']== 'mpi-bulk') & (df['ncpu'] == 48 * 2) ]
    mpi_bulk_4node = df[(df['framework']== 'mpi-bulk') & (df['ncpu'] == 48 * 4) ]
    mpi_bulk_8node = df[(df['framework']== 'mpi-bulk') & (df['ncpu'] == 48 * 8) ]
    mpi_bulk_1node['framework'] = 'MPI bulk sync 1 node'
    mpi_bulk_2node['framework'] = 'MPI bulk sync 2 nodes'
    mpi_bulk_4node['framework'] = 'MPI bulk sync 4 nodes'
    mpi_bulk_8node['framework'] = 'MPI bulk sync 8 nodes'


    mpi_openmp_1node = df[(df['framework']== 'mpi-openmp') & (df['ncpu'] == 48 * 1) ]
    mpi_openmp_2node = df[(df['framework']== 'mpi-openmp') & (df['ncpu'] == 48 * 2) ]
    mpi_openmp_4node = df[(df['framework']== 'mpi-openmp') & (df['ncpu'] == 48 * 4) ]
    mpi_openmp_8node = df[(df['framework']== 'mpi-openmp') & (df['ncpu'] == 48 * 8) ]
    mpi_openmp_1node['framework'] = 'MPI-OpenMP 1 node'
    mpi_openmp_2node['framework'] = 'MPI-OpenMP 2 nodes'
    mpi_openmp_4node['framework'] = 'MPI-OpenMP 4 nodes'
    mpi_openmp_8node['framework'] = 'MPI-OpenMP 8 nodes'


    openmp = df[(df['framework']== 'openmp') & (df['ncpu'] == 48 * 1) ]
    openmp['framework'] = 'OpenMP 1 node'
###################################################################################
    # hpx distributed using jemalloc (plain MPI); hpx local using tcmalloc
    df = pd.DataFrame(columns=['framework', 'ncpu', 'iter', 'elapsed', 'flops'])
    for f in sorted(all_hpx_files):
        f_split = f.split("-")
        n = len(f_split)
        idx = n - 2
        framework = f_split[0:idx]
        framework = "-".join(framework)
        ncpu = 48 * int(f_split[idx][0])
        
        parse_result(join(hpx_input_dir, f), df, ncpu, framework)
    df.to_csv(hpx_output_dir, index=False)
    
    hpx_jemalloc_1node = df[(df['framework']== 'hpx-plainmpi-join') & (df['ncpu'] == 48 * 1) ]
    hpx_jemalloc_2node = df[(df['framework']== 'hpx-plainmpi-join') & (df['ncpu'] == 48 * 2) ]
    hpx_jemalloc_4node = df[(df['framework']== 'hpx-plainmpi-join') & (df['ncpu'] == 48 * 4) ]
    hpx_jemalloc_8node = df[(df['framework']== 'hpx-plainmpi-join') & (df['ncpu'] == 48 * 8) ]
    hpx_jemalloc_1node['framework'] = 'HPX distributed 1 node'
    hpx_jemalloc_2node['framework'] = 'HPX distributed 2 nodes'
    hpx_jemalloc_4node['framework'] = 'HPX distributed 4 nodes'
    hpx_jemalloc_8node['framework'] = 'HPX distributed 8 nodes'


    hpx_local_tcmalloc_1node = df[(df['framework']== 'hpx-local-join') & (df['ncpu'] == 48 * 1) ]
    hpx_local_tcmalloc_1node['framework'] = 'HPX local 1 node'


    plot_err_band_all_1node(charm_1node, mpi_nonblock_1node, mpi_bulk_1node, mpi_openmp_1node, hpx_jemalloc_1node, 
        hpx_local_tcmalloc_1node, openmp)
    plot_err_band_all_2_node(charm_2node, mpi_nonblock_2node, mpi_bulk_2node, mpi_openmp_2node, hpx_jemalloc_2node)
    plot_err_band_all_4_node(charm_4node, mpi_nonblock_4node, mpi_bulk_4node, mpi_openmp_4node, hpx_jemalloc_4node)
    plot_err_band_all_8_node(charm_8node, mpi_nonblock_8node, mpi_bulk_8node, mpi_openmp_8node, hpx_jemalloc_8node)






