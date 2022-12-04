#!/bin/bash

test -e ssshtest || wget -q 'https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest'
. ssshtest

echo "Checking that program runs and produces expected output"
run deductive_analysis python ../deductive_analysis.py \
    --word_list_file_name ../data_files/sim_word_list.txt \
    --questions_file_name ../data_files/sim_ques.txt \
    --data_folder ../data_files \
    --current_transcripts_folder transcripts_no_audio_1st_five \
    --graphs_folder ../graphs
assert_in_stdout sim_int_1 {'good': 2, 'well': 2, 'interested': 4, 'available': 1, 'listened': 1, 'praising': 1}
assert_in_stdout sim_int_2 {'good': 1, 'well': 2, 'interested': 1, 'interesting': 2, 'available': 1, 'listened': 1, 'praising': 1}
assert_in_stdout sim_int_3 {'good': 1, 'well': 4, 'interested': 1, 'interesting': 2, 'available': 1, 'listened': 1, 'enjoyed': 3, 'praising': 1}
assert_in_stdout sim_int_4 {'good': 2, 'well': 3, 'interesting': 2, 'available': 1, 'listened': 1, 'praising': 1}
assert_in_stdout sim_int_5 {'good': 2, 'well': 3, 'available': 1, 'listened': 1, 'enjoyed': 1, 'praising': 1}
assert_in_stdout "{'good': 8, 'well': 14, 'interested': 6, 'available': 5, 'listened': 5, 'praising': 5, 'interesting': 6, 'enjoyed': 4}"


echo "Checking that there are no errors"
assert_exit_code 0

echo "Checking that all graphs were produced"
FILE=../graphs/sim_int_1_word_freq.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=../graphs/sim_int_2_word_freq.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=../graphs/sim_int_3_word_freq.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=../graphs/sim_int_4_word_freq.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=../graphs/sim_int_5_word_freq.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=../graphs/total_freq_graph.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi
