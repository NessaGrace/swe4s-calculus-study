#!/bin/bash

test -e ssshtest || wget -q 'https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest'
. ssshtest

run linear_search python search.py --search_type linear
assert_in_stdout 0
assert_exit_code 0

run binary_search python search.py --search_type binary
assert_in_stdout 0
assert_exit_code 0


run mean_threshold python search.py --search_type linear
assert_in_stdout [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], \
                  [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], \
                  [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], \
                  [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], \
                  [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]] \
                  ['Group 1', 'Group 3', 'Group 5', 'Group 7', 'Group 9', \
                  'Group 11', 'Group 13', 'Group 15', 'Group 17', 'Group 19', \
                  'Group 21', 'Group 23', 'Group 25', 'Group 27', 'Group 29', \
                  'Group 31', 'Group 33', 'Group 35', 'Group 37', 'Group 39']
assert_exit_code 0

run plot_gtex python plot_gtex.py \
    --gene_reads_file_name GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
    --sample_attributes_file_name GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
    --gene_name ACTA2 \
    --output_file_name_all ACTA2.bs.png \
    --output_file_name_high high_count.bs.png \
    --mean_threshold 100000

FILE=high_count.bs.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

FILE=ACTA2.bs.png
if test -f "$FILE"; then
    echo "$FILE exists."
fi

#assert_exit_code 0
