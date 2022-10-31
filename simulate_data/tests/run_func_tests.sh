test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_entire python simulate_data/create_data.py \
--write_file_name 'simulate_data/sim_data/func_test_sim_data.csv' \
--param_file_name 'simulate_data/input/parameters.txt' \
--sample_size '200' \
--param_delim '\t'
assert_exit_code 0
rm 'simulate_data/sim_data/func_test_sim_data.csv'