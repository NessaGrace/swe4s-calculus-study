#!/bin/bash

set -e
set -u
set -o

python -m unittest simulate_data/tests/test_utils.py

./simulate_data/tests/run_func_tests.sh
