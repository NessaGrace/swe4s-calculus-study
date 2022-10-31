#!/bin/bash

test -e ssshtest || wget -q 'https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest'
. ssshtest

# tests the function functions_lib.file_reader()
run file_reader python ../read_files.py --file_name ../data_files/sample/random_word_list.txt

assert_in_stdout "['two', 'red', 'magenta', 'pool', 'rent', 'orange', 'five', 'broadway', 'theater', 'theatre', 'joy', 'bro', 'chica', 'purple', 'work', 'lyric', 'ordinary', 'life', 'rock', 'in', 'the']"
assert_exit_code 0

# tests execution of the main script
run deductive python ../deductive.py \
    --word_list_file_name ../data_files/sim_word_list.txt \
    --questions_file_name ../data_files/sim_ques.txt

assert_exit_code 0
