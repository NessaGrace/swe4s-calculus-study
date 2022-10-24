#!/bin/bash

test -e ssshtest || wget -q 'https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest'
. ssshtest

run file_reader python ../read_files.py --file_name ../random_word_list.txt
#assert_stdout
assert_in_stdout "['two', 'red', 'magenta', 'pool', 'rent', 'orange', 'five', 'broadway', 'theater', 'theatre', 'joy', 'bro', 'chica', 'purple', 'work', 'lyric', 'ordinary', 'life', 'rock', 'in', 'the']"
#assert_in_stdout ['two', 'red', 'magenta', 'pool', 'rent', 'orange', 'five', 'broadway', 'theater', 'theatre', 'joy', 'bro', 'chica', 'purple', 'work', 'lyric', 'ordinary', 'life', 'rock', 'in', 'the']
#assert_in_stdout [two, red, magenta, pool, rent, orange, five, broadway, theater, theatre, joy, bro, chica, purple, work, lyric, ordinary, life, rock, in, the]
#assert_in_stdout ['two', 'red', 'magenta', 'pool', 'rent', 'orange', 'five',\
  #                'broadway', 'theater', 'theatre', 'joy', 'bro', 'chica',\
  #                'purple', 'work', 'lyric', 'ordinary', 'life', 'rock',\
   #               'in', 'the']

assert_exit_code 0

run deductive python ../deductive.py \
    --transcript_file_name ../sample_interview_text_with_questions.txt \
    --word_list_file_name ../random_word_list.txt \
    --questions_file_name ../sample_question_list.txt

assert_exit_code 0
