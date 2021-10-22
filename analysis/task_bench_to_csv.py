import click
import re
import glob
import pandas as pd
import numpy as np

@click.command()
@click.option('--input', type=str, help="Input directory with '.txt' files to parse")
@click.option('--output', type=str, help="Output file to write")
def main(input, output):
    input_files = glob.glob(f'{input}/*.txt')
    print(f"Found {len(input_files)} to parse.")
    columns=['NCPU', 'WIDTH', 'NITER', 'FLOPS']
    output_df = pd.DataFrame(columns=columns)

    for f in input_files:
        # add rows to the output dataframe
        data = pd.DataFrame(parse_file(f))
        output_df = pd.concat([output_df,data])

    output_df.to_csv(output, index=False)



def parse_file(f):
    header_re = re.compile('(-n (\d+))[\S\s]+(-width (\d+))[\S\s]+(-iter (\d+))')
    flops_re = re.compile('FLOP\/s (\d+.\d+(e\+\d+){0,1})')
    output=list()
    with open(f, 'r') as of:
        for line in of:
            if header_re.search(line):
                match = header_re.search(line)
                groups = match.groups(1)
                ncpu = int(groups[1])
                width = int(groups[3])
                niter = int(groups[5])
            elif flops_re.search(line):
                match = flops_re.search(line)
                flops = float(match.groups(1)[0])
                new_dict = {'NCPU':ncpu, 'WIDTH':width,
                            'NITER':niter,'FLOPS':flops}
                output.append(new_dict)
    return output




if __name__ == '__main__':
    main()
