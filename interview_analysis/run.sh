#!/bin/bash

set -e
set -u
set -o pipefail

echo "Checking new Python scripts against PEP8"
pycodestyle ..\test_functions_lib.py --show-source
pycodestyle deductive.py --show-source
pycodestyle functions_lib.py --show-source
pycodestyle read_files.py --show-source

echo "Running unit tests"
python ..\test_functions_lib.py

echo "Running functional tests"
bash ..\functional_tests.sh
