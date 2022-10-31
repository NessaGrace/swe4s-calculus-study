test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_entire python create_data.py \
--write_file_name 'sim_data/func_test_sim_data.csv' \
--param_file_name 'input/parameters.txt' \
--sample_size '200' \
--param_delim '\t'
assert_exit_code 0
rm 'sim_data/func_test_sim_data.csv'