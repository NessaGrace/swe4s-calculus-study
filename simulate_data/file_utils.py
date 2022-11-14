import numpy as np
import csv
import random
import pdb
import sys
import os


# Ensure that the sum of the list of probabilities for each question = 1
def check_sum(probability):
    if probability is None:
        return None
    if len(probability) == 0:
        return None

    sum = 0
    for iAns in range(len(probability)):
        sum += float(probability[iAns])

    return sum


# Read data from parameters.txt file
def read_data(file_name):
    # Lists of parameters to generate + questions
    question_header = []
    answer_header = []
    probability = []
    tolerance = 1e-3  # Tolerance for summation of probabilities

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
                # May have extra blank lines when exporting Excel files
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
            raise ArithmeticError('Warning: Probabilities of Question '
                                  + str(iQ) + ' does not ' + 'add to 1.')

    f_read.close()

    return question_header, answer_header, probability


# Write simulated data to .csv file
def write_data(file_name, question_header, answer_header, probability, size):
    # Write simulated data to file
    with open(file_name, 'w', newline='') as f_write:
        writer = csv.writer(f_write)
        writer.writerow(question_header)

        for iSamp in range(0, size):  # Create int(size) simulated students
            sample = []
            # For each question, randomly choose answer
            for iQuest in range(0, len(question_header)):
                rand_no = random.random()  # Random number between 0 and 1 (Rf)
                # Probability of having first answer is first probility (P1)
                curr_prob = float(probability[iQuest][0])
                ans_idx = 0  # Index of current answer
                not_accept = True  # Are we accepting answer?
                while (not_accept):
                    # If Rf < P1, accept answer
                    if (rand_no < curr_prob):
                        not_accept = False
                        sample.append(answer_header[iQuest][ans_idx])
                    # If Rf > P1, reject answer
                    else:
                        ans_idx += 1
                        # By adding P1 + P2, we are checking if P1 < Rf < P2
                        curr_prob += float(probability[iQuest][ans_idx])
            writer.writerow(sample)

    return 0


# FOR UNIT TESTING: Count frequency of each answer
def count_data(file_name, question_header, answer_header, probability, size):
    # Read simulated data from file
    try:
        f_read = open(file_name, 'r')
    except Exception:
        raise FileNotFoundError('Written data file name not found.')

    # Create m x n matrix of 0s to store counts of each answer
    m = len(question_header)
    n = len(answer_header)
    answer_counts = [[0 for x in range(n)] for x in range(m)]

    iter = 0
    if (os.path.getsize(file_name) > 0):
        for row in f_read:
            if (row):
                info = row.rstrip().split(',')

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

    f_read.close()
    # Normalize answer_counts to get probabilities
    for iQ in range(0, len(question_header)):
        for iAns in range(0, len(answer_header)):
            answer_counts[iQ][iAns] = answer_counts[iQ][iAns]/size

    return answer_counts
