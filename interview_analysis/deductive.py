""" Interview analysis script using deductive analysis

    * functions will go here
"""

#TODO: -replace sample data with simulated data
#      - account for additional questions that may come up
#      - account for lower/uppercase
#      - account for punctuation
#      - word fragments like "rent" vs. "apparently" - both contain "rent"
#        (may not be a problem - exact matches only, may miss plurals, etc)
#      - account for different spellings and meanings of words,
#      - account for how accurate audio is,
#      - think of other cases for searches that return bad results and
#        handle with test-driven development
#      - need to make word_list research-based, replace sample file
#      - must have phrases in word_list too

# Note: files are read in as paragraphs, not lines

import argparse
import string
import matplotlib.pyplot as plt
import numpy as np

from functions_lib import file_reader as fr

def main():
    parser = argparse.ArgumentParser(
                      description='reads in transcript, word list files',
                      prog='deductive')

    parser.add_argument('--transcript_file_name',
                        type=str,
                        help='Name of interview transcript file',
                        required=True)

    parser.add_argument('--word_list_file_name',
                        type=str,
                        help='Name of file with word list',
                        required=True)

    parser.add_argument('--questions_file_name',
                        type=str,
                        help='Name of file with questions',
                        required=True)

    args = parser.parse_args()

    # read in questions_file
    try:
        questions_list = fr(args.questions_file_name)
    except FileNotFoundError as e:
        print('could not find ' + args.questions_file_name)
        sys.exit(1)
    except Exception as e:
        print('error of type ' + str(type(e)) + ' occurred')
        sys.exit(1)

    # read in transcript file
    try:
        transcript = fr(args.transcript_file_name)
    except FileNotFoundError as e:
        print('could not find ' + args.transcript_file_name)
        sys.exit(1)
    except Exception as e:
        print('error of type ' + str(type(e)) + ' occurred')
        sys.exit(1)

    # remove questions from transcript
    answers = []

    for line in transcript:
        if line not in questions_list:
            answers.append(line)

    answer_words = []
    for answer in answers:
        answer_words.append(answer.split())

    answer_word_list = [answer_word for sublist in answer_words for answer_word in sublist]

    answer_word_list_no_punc = []
    # punc = '''!()[]{};:'"\,<>./?@#$%^&*_~“”''' # note: may need to update,
                                                # not sure what is saved by
                                                # audio, check in unittest

    for answer_word in answer_word_list:
        # uses string method to remove most punctuation (except apostrophes/quotes, some formats)
        answer_word_list_no_punc.append(answer_word.translate(str.maketrans('', '', string.punctuation)))

    ans_word_list_no_quotes = [] # add conditions for hyphens, contractions based on audio results

    for answer_word in answer_word_list_no_punc:
        ans_word_list_no_quotes.append(answer_word.replace("“", "").replace("”", ""))

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
    #print(word_counter)

    # make list of words in word_counter:
    #word_matches = []
    #for key in word_counter:
     #   word_matches.append(key)

    # plot word frequency for words in list:
    word_matches = list(word_counter.keys())
    counts = list(word_counter.values())

    fig = plt.figure(figsize = (10, 5))
    plt.bar(word_matches, counts, color='thistle', width=0.4)
    plt.xlabel("Word from Word List")
    plt.ylabel("Frequency in Interview Data")
    plt.title("Word Frequency in Interview Data")
    plt.show()


if __name__ == '__main__':
    main()
