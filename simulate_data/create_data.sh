#!/bin/bash

set -e
set -u
set -o pipefail

python create_data.py \
--write_file_name 'sim_data/test_sim_data.csv' \
--param_file_name 'input/parameters.txt' \
--sample_size '200' \
--param_delim '\t'