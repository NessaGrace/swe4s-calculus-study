#!/bin/bash

test -e ssshtest || wget -q 'https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest'
. ssshtest

echo "Checking that program runs and produces expected output"
run deductive_analysis python ../deductive_analysis.py \
    --word_list_file_name ../data_files/sim_word_list.txt \
    --questions_file_name ../data_files/sim_ques.txt \
    --data_folder ../data_files \
    --current_transcripts_folder transcripts_no_audio_last_five \
    --graphs_folder ../graphs
assert_in_stdout sim_int_10 {'interested': 1}
assert_in_stdout sim_int_6 {'interested': 1}
assert_in_stdout sim_int_7 {'good': 1, 'well': 1, 'interested': 3, 'available': 1}
assert_in_stdout sim_int_8 {'good': 1, 'well': 2, 'interested': 1}
assert_in_stdout sim_int_9 {'interested': 1}
assert_in_stdout sim_int_sample {'interested': 1}
assert_in_stdout "{'interested': 8, 'good': 2, 'well': 3, 'available': 1}"


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
