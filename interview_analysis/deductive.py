""" Interview analysis script using deductive analysis

    * functions will go here
"""

#TODO: -replace sample data with simulated data
#      - account for additional questions that may come up
#      - account for lower/uppercase
#      - account for punctuation
#      - word fragments like "rent" vs. "apparently" - both contain "rent"
#      - account for different spellings and meanings of words,
#      - account for how accurate audio is,
#      - think of other cases for searches that return bad results and
#        handle with test-driven development
#      - need to make word_list research-based, replace sample file
#      - must have phrases in word_list too

# Keep for formatting for now: A = A.append(line.rstrip().split('\n'))


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

    # read in transcript file
    transcript_file = open(args.transcript_file_name, 'r')

    # read in questions_file
    

    # note: lines read in as the entire Q or A (not by indiv. lines)
    for line in transcript_file:
        if

    f.close()

    #print(A)

    # read in word list file
    #g = open(args.word_list_file_name, 'r')

    #for line in g:
     #   print(line)
    #    B = line.rstrip().split(',')

    #g.close()


if __name__ == '__main__':
    main()
