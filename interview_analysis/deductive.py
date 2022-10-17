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

# Keep for formatting for now: A = A.append(line.rstrip().split('\n'))
# Note: files are read in as paragraphs, not lines

import argparse
import string

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
    questions_list = fr(args.questions_file_name)
    # print(questions_list)

    # read in transcript file
    transcript = fr(args.transcript_file_name)
    # print(transcript)

    # remove questions from transcript
    answers = []

    for line in transcript:
        # line.replace(u'\xa0', u' ') # implement later?
        if line not in questions_list:
            answers.append(line)

    # print(answers)

    answer_words = []
    for answer in answers:
        answer_words.append(answer.split())
    #print(answer_words)

    answer_word_list = [answer_word for sublist in answer_words for answer_word in sublist]
    # print(answer_word_list)

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

    #print(ans_word_list_no_quotes)

    # read in word list file
    word_list = fr(args.word_list_file_name)
    #print(word_list)

    # initialize word_counter dictionary
    word_counter = {}

    # count instances of words in word_list in transcript
    for word1 in word_list:
        for word2 in ans_word_list_no_quotes:
            #if word not in word_counter:
            if word1 == word2:
                try:
                    word_counter[word1] += 1
                except KeyError:
                    word_counter[word1] = 1
        #else:
            #word in ans_word_list_no_quotes and word in word_counter:
         #   word_counter[word] += 1
    print(word_counter) # "the" is being miscounted (doubled), need to fix


if __name__ == '__main__':
    main()
