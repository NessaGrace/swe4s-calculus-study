import numpy as np
import csv
import argparse
import random
import pdb
import sys


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

    # Lists of parameters to generate + questions
    question_header = []
    answer_header = []
    probability = []
    tolerance = 1e-6

    # Go through parameter file, fill lists
    try:
        f_read = open(args.param_file_name)
    except:
        print('Input parameter file name not found. Exiting...')
        sys.exit(1)

    # Read questions, answers, and probabilities from parameter file
    iter = 0
    for row in f_read:
        info = row.rstrip().split('\t') # TODO why not argument?
        if (len(info) > 0):
            continue
        else: 
            print('WARNING: Line ' + str(iter + 1) + ' is empty. Exiting...')
            sys.exit(1)

        if (iter % 2 == 0):
            question_header.append(info[0])
            answer_header.append(info[1:])
        else:
            probability.append(info[1:])
        iter += 1

    # Check whether probabilities of all questions add to 1
    for iQ in range(0, len(question_header)):
        sum = 0
        for iAns in range(0, len(probability[iQ])):
            sum += float(probability[iQ][iAns])
        if abs(sum - 1) > tolerance:  # Sum = 1 within tolerance
            print('Warning: Probabilities of Question ' + str(iQ) + ' does not '
                  + 'add to 1. Exiting...')
            sys.exit(1)

    # Write simulated data to file
    with open(args.write_file_name, 'w', newline='') as f_write:
        writer = csv.writer(f_write)
        writer.writerow(question_header)

        for iSamp in range(0, args.sample_size):
            sample = []
            for iQuest in range(0, len(question_header)):
                rand_no = random.random()
                curr_prob = float(probability[iQuest][0])
                ans_idx = 0
                not_accept = True

                while (not_accept):
                    if (rand_no < curr_prob):
                        not_accept = False
                        sample.append(answer_header[iQuest][ans_idx])
                    else:
                        ans_idx += 1
                        curr_prob += float(probability[iQuest][ans_idx])
            writer.writerow(sample)


if __name__ == '__main__':
    main()
