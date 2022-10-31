import numpy as np
import csv
import random
import pdb
import sys
import os


def check_sum(probability):
    tolerance = 1e-6
    if probability is None:
        return None
    if len(probability) == 0:
        return None

    sum = 0
    for iAns in range(len(probability)):
        sum += probability[iAns] 

    return sum

def read_data(file_name):
    # Lists of parameters to generate + questions
    question_header = []
    answer_header = []
    probability = []

    # Go through parameter file, fill lists
    try:
        f_read = open(file_name, 'r')
    except Exception:
        raise FileNotFoundError('Input parameter file name not found.')

    # Read questions, answers, and probabilities from parameter file
    iter = 0
    if (os.path.getsize(file_name) > 0):
        for row in f_read:
            if (row):
                info = row.rstrip().split('\t')  # TODO why not argument?
            else:
                f_read.close()
                raise IndexError('File empty.')

            # If list does not contain first entry, must be blank
            if (info[0]):
                if (iter % 2 == 0):
                    question_header.append(info[0])
                    answer_header.append(info[1:])
                else:
                    probability.append(info[1:])
                iter += 1
            else:
                f_read.close()
                raise IndexError('WARNING: Line ' + str(iter + 1)
                                 + ' is empty.')
    else:
        f_read.close()
        raise TypeError('File is empty.')

    # Check whether probabilities of all questions add to 1
    for iQ in range(0, len(question_header)):
        sum = check_sum(probability[iQ])
        if abs(sum - 1) > tolerance:  # Sum = 1 within tolerance
            f_read.close()
            raise ArithmeticError('Warning: Probabilities of Question ' + str(iQ)
                                  + ' does not ' + 'add to 1.')

    f_read.close()

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


def count_data(file_name, question_header, answer_header, probability, size):
    # Read simulated data from file
    try:
        f_read = open(file_name, 'r')
    except Exception:
        raise FileNotFoundError('Written data file name not found.')

    # Create m x n matrix of 0s to store counts of certain answers
    m = len(question_header)
    n = len(answer_header)
    answer_counts = [[0 for x in range(n)] for x in range(m)]

    iter = 0
    if (os.path.getsize(file_name) > 0):
        for row in f_read:
            if (row):
                info = row.rstrip().split(',')  # TODO why not argument?

                if (iter == 0):
                    pass  # Ignore question header
                else:
                    for iQ in range(0, len(question_header)):
                        for iAns in range(0, len(answer_header)):
                            # Check if written data matches answer
                            if info[iQ] == answer_header[iQ][iAns]:
                                answer_counts[iQ][iAns] += 1
                                break  # Get out of for loop
                            else:
                                pass  # Keep checking answers
            else:
                f_read.close()
                raise IndexError('File empty.')
            iter += 1
    else:
        f_read.close()
        raise TypeError('File is empty.')

    return 0
