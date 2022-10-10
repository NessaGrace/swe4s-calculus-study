""" Interview analysis script using deductive analysis

    * functions will go here
"""

import argparse

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

    args = parser.parse_args()

    #TODO: currently sample interview data in f, replace w/ simulated data,
    # need to exclude the questions but also divide by them, account
    # for additional questions that may come up, account for lower/upper,
    # account for punctuation, may need to use sample audio file that
    # had speech to text done on it too, word fragments like "rent" vs.
    # "apparently" - both contain "rent", worry about different spellings
    # and meanings of words, worry about how accurate audio is, think of
    # other cases for searches that return bad results and add them in with
    # time (test-driven development)

    f = open(args.transcript_file_name, 'r')

    A = []
    print(type(A))

    for line in f:
        #print(line)
        A = A.append(line.rstrip().split('\n')) # something is wrong in this line

    f.close()

    print(A)

    #TODO: currently random word list in g, replace w/ researched word list
    # current random list has some words in, some out of interview script,
    # will need to add phrases eventually

    # THE CODE BELOW IS NOT COMPLETE

    print()
    g = open(args.word_list_file_name, 'r')

    for line in g:
        print(line)
    #    B = line.rstrip().split(',')

    g.close()

    #for i in A:
     #   for j in B:
      #      if B[j] in A[i] # will need to be if STRINGS in B[j] in A[i]

if __name__ == '__main__':
    main()
