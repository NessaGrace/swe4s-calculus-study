# STEM Retention by Race, Ethnicity, and Gender after Calculus I

> For more detailed descriptions of each directory's software, please refer to the README files in the individual directories. Specifically, there is a README in each of the simulate_data, interview_analysis, and survey_analysis directories.

TODO Add pretty pictures

The purpose of this study is to. There is a survey, and an interview, etc. TODO

This software is divided into three directories. `simulate_data` creates simulated Google Forms survey data in order to test the survey analysis software. Answers are chosen according to prescribed probabilities, and each answer has an associated "correlation" with whether or not the student will choose to take Calculus II. `survey_analysis` filters the survey data for the inputted demographic, then finds the probability they will continue on to Calculus II.

`interview_analysis` uses deductive analysis by searching an interview transcript for words from a pre-determined list and counts the frequency of each word.

## Dependencies 

numpy, argparse, pycodestyle, pandas, matplotlib TODO Fill out any others

## Usage example

##### For Simulated Data

```
python create_data.py \
    --write_file_name 'sim_data/test_sim_data.csv' \
    --param_file_name 'input/parameters.txt' \
    --sample_size '200' \
    --param_delim '\t'`
```

![](sim_data/readme_images/sim_data_image.png)

##### For Survey Analysis 

```
python probability.py \
    --file_name test_sim_data.csv \
    --gender_identity [cis-W, trans_W] \
    --race_ethnicity [black]
```

##### For Interview Analysis

```
python deductive.py
    --word_list_file_name data_files/sim_word_list.txt
    --questions_file_name data_files/sim_ques.txt
```
