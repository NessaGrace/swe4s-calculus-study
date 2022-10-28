#!/bin/bash

# test probaility.py - make sure file is outputted
python probability.py \
    --file_name test_sim_data.csv \
    --gender_identity trans_W cis_W \
    --race_ethnicity white black asian \

if [ -f "./probabilities_bar.png" ];
then
    echo "File probabilities_bar.png exists"
else 
    echo "File probabilities_bar.png does not exist"
fi