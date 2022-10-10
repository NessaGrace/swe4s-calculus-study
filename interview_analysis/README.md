# Directory Description:

This directory creates the interview analysis software. Currently,
there are two sample text files, sample_interview_text_with_questions.txt
and random_word_list.txt. The first will later be replaced with simulated
interview data and will be used to test many different cases, including 
speech-to-text generated transcripts to test transcription accuracy, words 
present in the text, words not present in the text, and words that contain 
the same fragments such as "an" and "and", among others. The second file 
will be replaced with research-based words to search for in the interview
transcripts that are related to retention in STEM. The Python script
deductive.py will search for words/phrases from random_word_list.txt present
in sample_interview_text_with_questions.txt. 

# How to Run Code:
python deductive.py \
    --transcript_file_name sample_interview_text_with_questions.txt \
    --word_list_file_name random_word_list.txt
