import numpy as np
import csv
import argparse
import random
import pdb


def main():
    # Receive input from command line
    parser = argparse.ArgumentParser()
    # File name to write simulated data to (.csv only, 10/9/22)
    parser.add_argument('--write_file_name', type=str, required=True)
    # File name to take input parameters from
    parser.add_argument('--param_file_name', type=str, required=True)

    args = parser.parse_args()

    f_read = open(args.param_file_name, 'r')
    f_write = open(args.write_file_name, 'w')

    writer = csv.writer(f_write)

    

if __name__ == '__main__':
    main()
