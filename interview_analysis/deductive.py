""" Interview analysis script using deductive analysis

    * functions_lib.file_reader - reads file and stores contents in list
"""

# TODO: - add more frequency stats? rel freq?
#       - account for additional questions that may come up during interview?
#       - account for punctuation in audio
#       - fix: currently finds exact matches only, may miss plurals, etc
#       - account for different spellings/meanings/formats (e.g. 1 vs one vs i)
#       - in word list, include multiple versions of word? (e.g. yes vs yeah)
#       - in word list, consider contractions/possessives/hyphens, etc
#       - account for how accurate audio is
#       - think of other cases for searches that return bad results and
#         handle with test-driven development
#       - need to make word_list research-based at some point
#       - must fix program to pick up on phrases in word list too
#       - need to get total_word_counter working to look at plots/stats overall
#       - need to update code to process the first 5 responses as demographics
#       - need more functions?
#       - look at word freq by question - implement if time
#       - differences in transcripts 1-5 vs. 6-10 - is that ok for simulation?
#       - current transcript files do not have questions - will need to fix

# Note: files are read in as paragraphs, not lines

import argparse
import string
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
import os
import sys

from functions_lib import file_reader as fr


def main():
    parser = argparse.ArgumentParser(
                      description='reads in transcript, word list files',
                      prog='deductive')

    parser.add_argument('--word_list_file_name',
                        type=str,
                        help='Name of file with word list',
                        required=True)

    parser.add_argument('--questions_file_name',
                        type=str,
                        help='Name of file with questions',
                        required=True)

    args = parser.parse_args()

    # read in file with questions list
    try:
        questions_list = fr(args.questions_file_name)
    except FileNotFoundError as e:
        print('could not find ' + args.questions_file_name)
        sys.exit(1)
    except Exception as e:
        print('error of type ' + str(type(e)) + ' occurred')
        sys.exit(1)

    # TODO: finish this later on
    # total_word_counter = {}

    # read in all transcripts at once for processing:

    # gets file path where all transcripts stored
    transcript_file_location = os.path.join('data_files',
                                            'transcripts_no_audio',
                                            '*.txt')
    transcript_files = glob.glob(transcript_file_location)

    # gets file identifier for each file in path
    for file in transcript_files:
        file_name = os.path.basename(file)
        split_filename = file_name.split('.')
        interview_num = split_filename[0]

        # reads file contents and stores in transcript list
        try:
            transcript = fr(file)
        except FileNotFoundError as e:
            print('could not find ' + args.questions_file_name)
            sys.exit(1)
        except Exception as e:
            print('error of type ' + str(type(e)) + ' occurred')
            sys.exit(1)

        # remove questions from transcript
        answers = []

        try:
            for line in transcript:
                if line not in questions_list:
                    answers.append(line)
        except Exception as e:
            print('error of type ' + str(type(e)) + ' occurred')
            sys.exit(1)

        # split list of answer sentences into list of answer words
        ans_words = []

        try:
            for answer in answers:
                ans_words.append(answer.split())
            # converts ans_words to list instead of list of lists
            ans_word_lst = [ans_word for sub in ans_words for ans_word in sub]
        except Exception as e:
            print('error of type ' + str(type(e)) + ' occurred')
            sys.exit(1)

        # remove punctuation from ans_word_lst
        no_punc = []

        # save this for now:
        # punc = '''!()[]{};:'"\,<>./?@#$%^&*_~“”'''

        try:
            for ans_word in ans_word_lst:
                # uses string method to remove most punctuation (except
                # apostrophes/quotes, some formats)
                no_punc.append(ans_word.translate(str.maketrans('', '', string.punctuation)))  # nopep8

            # removes quotes/apostrophes with different format and other
            # undesired symbols
            ans_word_list_no_quotes = []
            for answer_word in no_punc:
                ans_word_list_no_quotes.append(answer_word.replace("“", "").replace("”", "").replace("’", "").replace("â€™", ""))  # nopep8
        except Exception as e:
            print('error of type ' + str(type(e)) + ' occurred')
            sys.exit(1)

        # read in word list file
        try:
            word_list = fr(args.word_list_file_name)
        except FileNotFoundError as e:
            print('could not find ' + args.word_list_file_name)
            sys.exit(1)
        except Exception as e:
            print('error of type ' + str(type(e)) + ' occurred')
            sys.exit(1)

        # initialize word_counter dictionary
        word_counter = {}

        # count instances of words in word_list in transcript
        for word1 in word_list:
            for word2 in ans_word_list_no_quotes:
                if word1 == word2:
                    try:
                        word_counter[word1] += 1
                    except KeyError:
                        word_counter[word1] = 1
        print(interview_num, word_counter)

        # TODO: fix total_word_counter, so it works (unindented for PEP8)

        # get total word counts in all transcript files
        # for word1 in word_list:
        # for word2 in word_counter:
        # if word1 == word2:
        # try:
        # total_word_counter[word1] += word_counter[word2]
        # except KeyError:
        # total_word_counter[word1] = 1

        # plot word frequency for words in list for given transcript:
        word_matches = list(word_counter.keys())
        counts = list(word_counter.values())

        fig = plt.figure(figsize=(10, 5))
        plt.bar(word_matches, counts, color='thistle', width=0.4)
        plt.xlabel("Word from Word List")
        plt.ylabel("Frequency in Interview Data")
        plt.title("Word Frequency in Interview Data")
        # plt.show()
        plt.savefig('graphs/sim_int_' + interview_num + '_word_freq.png')

    # TODO: fix this
    # print(total_word_counter)


if __name__ == '__main__':
    main()
