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
    # File name to take input parameters from (.txt tab delimited only)
    parser.add_argument('--param_file_name', type=str, required=True)
    parser.add_argument('--param_delim', type=str, required=True)
    parser.add_argument('--sample_size', type=int, required=True)

    args = parser.parse_args()

    # Lists of parameters to generate + questions
    question_header = []
    answer_header = []
    probability = []

    # Go through parameter file, fill lists
    with open(args.param_file_name, 'r') as f_read:
        #reader = csv.reader(f_read, delimiter=',')#, quotechar='"', quoting=csv.QUOTE_ALL)
        iter = 0
        for row in f_read:
            list = row.split('\t')
            if (iter % 2 == 0):
                question_header.append(list[0])
                answer_header.append(list[1:])
            else:
                probability.append(list[1:]) # TODO Make probabilities add to 1
            iter += 1
    question_header.insert(0, 'Timestamp') # TODO Google forms adds time stamp

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
                        pdb.set_trace()
                        sample.append(answer_header[iQuest][ans_idx])
                    else:
                        ans_idx += 1
                        curr_prob += float(probability[iQuest][ans_idx])
            pdb.set_trace()
        

if __name__ == '__main__':
    main()
