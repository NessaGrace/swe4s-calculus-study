# Directory Description:

This directory creates the interview analysis software. The current type of
analysis is deductive analysis, wherein we search each interview transcript
for words from a pre-determined list and count the frequency of each word.
The main script is deductive.py, which relies on a number of dependencies,
including the libraries argparse, string, matplotlib.pyplot, numpy, pandas,
glob, sys, and os. It also uses the function file_reader(), which is contained
within functions_lib.py. This function reads a file and produces a list of
its lines as output and reduces redundancy in the code, where several files
must be processed. In practice, deductive.py reads in and processes multiple
interview transcript text files into lists of words that contain only
interview answers (i.e. not the questions) and no puncutation. Then, the
words in the list for each transcript are compared with the pre-determined
word list and a dictionary called word_counter is produced that gives the
count for each word in a given transcript. A word frequency plot is produced
for each transcript analyzed. In the future, there will be several
improvements made including adding more statistics to analyze trends between
transcripts and word frequency for all transcripts collectively.

# Unit and Functional Tests:

All tests are included in the sub-directory tests. The unit tests are
contained within test_functions_lib.py and test for expected output
with both lowercase and mixed-case examples, as well as checking that the
FileNotFoundError is raised appropriately. The unit tests utilize the
unittest, os, and sys libraries. The functional tests are contained
within functional_tests.sh and test for proper execution of both the 
file_reader() function and deductive.py. It uses the Stupid Simple baSh
testing framework, which is also included in the tests sub-directory, and
it also relies on the script read_files.py (located in the directory 
interview_analysis) in order to test the output from file_reader().

# How to Use the Project:

**Files**

In the directory data_files, the sub-directory sample contains a sample
interview script, a sample question list, and a sample word list. These 
files are not currently being used but are being retained in case they 
are needed for any sort of testing later on. \

The sub-directory transcripts_no_audio contains ten simulated interview
transcripts. The first 5 simulated interview scripts come from the OpenAI
tool and are biased. The next 5 are written responses to add more diversity
to the simulated data. The first 5 interview questions are related to the 
participant's identity. These will be processed separately from the word
counts related to their experiences in Calc 1. \

The files sim_word_list.txt and sim_ques.txt are the word list and question
list that are associated with the simulated interview data. \

The output from deductive.py is stored in the directory graphs. Currently,
this contains 10 bar graphs with word frequency for the simulated interviews.

**Examples**
Below are examples of how to run the files from within the directory
interview_analysis. \

To run the main script: \

python deductive.py \
    --word_list_file_name data_files/sim_word_list.txt \
    --questions_file_name data_files/sim_ques.txt

To run the unit tests: \

python tests/test_functions_lib.py \

To run the functional tests: \

bash functional_tests.sh

**Command Line Arguments/Parameters**
In deductive.py: \

    - word_list_file_name: the name of the current word list
      file being used \
    - questions_file_name: the name of the current question
      list file being used \

In read_files.py: \
    - file_name: the name of the file used to test file_reader()
      in functional_tests.sh

# How to Install the Software:
For this project, the following installations must be completed
in the command line: \
    - conda install numpy \
    - conda install pycodestyle \
    - conda install pandas \
    - conda install matplotlib \

 To run the functional tests using the Stupid Simple baSh Framework,
 you will also need to install the network utility `wget`. `wget` can
 be downloaded from http://gnuwin32.sourceforge.net/packages/wget.htm
 and will need to be installed with `conda install wget` prior to 
 running the functional tests.
