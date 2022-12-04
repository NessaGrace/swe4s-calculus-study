""" Interview analysis script using deductive analysis

    * fl.file_reader - reads file and stores contents in list
    * fl.filter_by_line - filters the contents of one list from another list
    * fl.sentence_splitter - splits list of multi-word strings into list of
                             single-word strings
    * fl.remove_punctuation - removes punctuation from list of strings
    * fl.word_counter - counts instances of words from a list in another list
                        of strings
"""

import argparse
import string
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
import os
import sys
import nltk  # nltk module will be used in the future

import functions_lib as fl


def main():
    parser = argparse.ArgumentParser(
                      description='counts words in files',
                      prog='deductive')

    parser.add_argument('--word_list_file_name',
                        type=str,
                        help='Name of file with word list',
                        required=True)

    parser.add_argument('--questions_file_name',
                        type=str,
                        help='Name of file with questions',
                        required=True)

    parser.add_argument('--data_folder_name',
                        type=str,
                        help='Name of data files folder for transcripts path',
                        required=True)

    parser.add_argument('--current_transcripts_folder',
                        type=str,
                        help='Name of transcript folder for transcripts path',
                        required=True)

    parser.add_argument('--graphs_folder',
                        type=str,
                        help='Name of directory to store output graphs in',
                        required=True)

    args = parser.parse_args()

    # read in file with questions list
    try:
        questions_list = fl.file_reader(args.questions_file_name)
    except FileNotFoundError as e:
        print(f"could not find {args.questions_file_name}")
        sys.exit(1)
    except Exception as e:
        print(f"error of type {type(e)} occurred")
        sys.exit(1)

    # initialize counter dictionary for words in all transcripts
    total_word_counter = {}

    # read in all transcripts at once for processing:

    # gets file path where all transcripts stored
    try:
        curr_transcript_loc = os.path.join(args.data_folder_name,
                                           args.current_transcripts_folder,
                                           '*.txt')
        current_transcript_files = glob.glob(curr_transcript_loc)
    except Exception as e:
        print(f"error of type {type(e)} occurred")
        sys.exit(1)

    # gets file identifier for each file in path
    try:
        for file in current_transcript_files:
            file_name = os.path.basename(file)
            split_filename = file_name.split('.')
            interview_num = split_filename[0]

            # reads file contents and stores in transcript list
            try:
                transcript = fl.file_reader(file)
            except FileNotFoundError as e:
                print(f"could not find transcript file")
                sys.exit(1)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # remove questions from transcript
            try:
                answers = fl.filter_by_line(transcript, questions_list)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # split list of answer sentences into list of answer words
            try:
                ans_words = fl.sentence_splitter(answers)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # remove punctuation from ans_words
            try:
                no_punc = fl.remove_punctuation(ans_words)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # read in word list file
            try:
                word_list = fl.file_reader(args.word_list_file_name)
            except FileNotFoundError as e:
                print(f"could not find {args.word_list_file_name}")
                sys.exit(1)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # count instances of words from word_list in transcript
            try:
                word_counter = fl.word_counter(word_list, no_punc)
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # print word counters for each transcript
            print(interview_num, word_counter)

            # get total word counts in all transcript files
            try:
                for key in word_counter:
                    if key in total_word_counter:
                        total_word_counter[key] += word_counter[key]
                    elif key not in total_word_counter:
                        total_word_counter[key] = word_counter[key]
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

            # plot word frequency for words in list for given transcript:
            try:
                word_matches = list(word_counter.keys())
                counts = list(word_counter.values())

                fig = plt.figure(figsize=(10, 5))
                plt.bar(word_matches, counts, color='thistle', width=0.4)
                plt.xlabel("Words")
                plt.ylabel("Frequency")
                plt.title("Word Frequency in Calculus Interviews")
                plt.savefig(args.graphs_folder +
                            "/" +
                            interview_num +
                            '_word_freq.png')
            except Exception as e:
                print(f"error of type {type(e)} occurred")
                sys.exit(1)

        # prints out total number of occurrences of each word from word_list
        # across all interviews
        print(total_word_counter)

        # plot total word frequencies across all transcripts:
        try:
            total_word_matches = list(total_word_counter.keys())
            total_counts = list(total_word_counter.values())

            fig = plt.figure(figsize=(10, 5))
            plt.bar(total_word_matches, total_counts, color='thistle',
                    width=0.4)
            plt.xlabel("Words")
            plt.ylabel("Frequency")
            plt.title("Word Frequency in Calculus Interviews")
            plt.savefig(args.graphs_folder + '/total_freq_graph.png')
        except Exception as e:
            print(f"error of type {type(e)} occurred")
            sys.exit(1)

    except Exception as e:
        print(f"error of type {type(e)} occurred")
        sys.exit(1)


if __name__ == '__main__':
    main()
