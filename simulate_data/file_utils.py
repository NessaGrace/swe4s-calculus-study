import numpy as np
import csv
import random
import pdb
import sys

def read_data(file_name):
    # Lists of parameters to generate + questions
    question_header = []
    answer_header = []
    probability = []
    tolerance = 1e-6

    # Go through parameter file, fill lists
    try:
        f_read = open(file_name)
    except Exception:
        raise OSError('Input parameter file name not found.')

    # Read questions, answers, and probabilities from parameter file
    iter = 0
    for row in f_read:
        info = row.rstrip().split('\t')  # TODO why not argument?
        if (len(info) > 0):
            continue
        else:
            raise IndexError('WARNING: Line ' + str(iter + 1) + ' is empty.')

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
            raise ArithmeticError('Warning: Probabilities of Question '
                                  + str(iQ) + ' does not ' + 'add to 1.')

    return question_header, answer_header, probability

def write_data(file_name, question_header, answer_header, probability, size):
    # Write simulated data to file
    with open(file_name, 'w', newline='') as f_write:
        writer = csv.writer(f_write)
        writer.writerow(question_header)

        for iSamp in range(0, size):
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

    return 0
