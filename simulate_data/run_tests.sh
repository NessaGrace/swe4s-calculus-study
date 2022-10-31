#!/bin/bash

set -e
set -u
set -o

python -m unittest tests/test_utils.py

./tests/run_func_tests.sh
