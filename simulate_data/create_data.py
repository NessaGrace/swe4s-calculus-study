import numpy as np
import csv
import argparse
import random
import pdb
import sys
import file_utils as util


def main():
    # Receive input from command line
    parser = argparse.ArgumentParser()
    # File name to write simulated data to (.csv only, 10/9/22)
    parser.add_argument('--write_file_name', type=str, required=True)
    # File name to take input parameters from (.txt tab delimited only)
    parser.add_argument('--param_file_name', type=str, required=True)
    parser.add_argument('--param_delim', type=str, required=True)
    # Statistically significant sample size: 200
    parser.add_argument('--sample_size', type=int, required=True)

    args = parser.parse_args()

    # Read data from file
    questions, answers, probability = util.read_data(args.param_file_name)

    # Write data to file
    util.write_data(args.write_file_name,
                    questions,
                    answers,
                    probability,
                    args.sample_size)


if __name__ == '__main__':
    main()
