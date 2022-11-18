# Visualize survey data - probability analysis
> For a given demographic, find the probability that that demographic
will continue on to Calculus II, based on the inputted survey data.

In this project we develop tools to analyze survey data. We filter the survey
data for the inputted demographic, and then find the probability they will
continue on to Calculus II.


## Usage example

Say we want to look at the probability that a black woman will continue on
to take Calculus II. Then we would run:

```sh
$ python probability.py \
    --file_name test_sim_data.csv \
    --gender_identity cis-W trans_W \
    --race_ethnicity black
```

The output will be a bar plot comparing the input demographic to all
survey respondents as well as men and women separately. 

## Available inputs for the command line arguments
* **--gender_identity:** cis_W, cis_M, trans_W, trans_M, non_binary, agender, intersex, gender_fluid, other
* **--race_ethnicity:** white, black, asian, native_amer_AK, pacific_isl, hisp_latx, 2+, other
* **--field:** stem, non-stem

## Command line argument descriptions
* **cis_W**: Cisgender woman
* **cis_M**: Cisgender man
* **trans_W**: Transgender woman
* **trans_M**: Transgender man
* **non_binary**: Non-binary (does not identify exclusively as a man or woman)
* **agender**: Agender (does not identify as any gender
* **intersex**: Intersex (has combination of male and female traits)
* **gender_fluid**: Gender fluid (gender identity is variable over time)
* **white**: White (non-Hispanic/Latinx)
* **black**: Black/African American (non-Hispanic/Latinx)
* **asian**: Asian/Asian American (non-Hispanic/Latinx)
* **native_amer_AK**: Indigenous/Native American/Native Alaskan (non-Hispanic/Latinx)
* **pacific_isl**: Native Hawaiian/Pacific Islander (non-Hispanic/Latinx)
* **hisp_latx**: Hispanic/Latinx
* **2+:** 2 or more races
* **other**: Other
* **stem**: Stem field. This includes: biology, chemistry, physics, mathematics, computer science/technology, engineering/architecture, economics, environmental science/studies, medicine/health, and earth/space science
* **non-stem**: Non-stem field. This includes: Education, performing arts, visual arts, social sciences, english/communication, philosophy, modern language, law/government, and social services