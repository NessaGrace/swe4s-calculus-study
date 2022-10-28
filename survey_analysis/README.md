# Visualize survey data - probability analysis
> For a given demographic, find the probability that that demographic
will continue on to Calculus II, based on the inputted survey data.

In this project we develop tools to analyze survey data. We filter the survey
data for the inputted demographic, and then find the probability they will
continue on to Calculus II.

## Installation

With Anaconda, simply run: 

```sh
conda install survey_analysis
```

## Usage example

Say we want to look at the probability that a black woman will continue on
to take Calculus II. Then we would run:

```sh
$ python probability.py \
    --file_name test_sim_data.csv \
    --gender_identity [cis-W, trans_W] \
    --race_ethnicity [black] \
```

The output will be a bar plot comparing the input demographic to all
survey respondents as well as men and women separately. 

## Release History

* v1.0
    * Initial version that creates a plot of the probability that a given
        demographic will take Calculus II in the future.