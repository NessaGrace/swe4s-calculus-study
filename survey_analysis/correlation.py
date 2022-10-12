# Goal: given a csv file of survey responses, find the correlation 
# that that demographic has to taking calc 2 in the future

# Inputs:
#   - The dataset to use
#   - The given demographic: 
#      - Select multiple options from:
#          - Gender identity
#          - Race/ethnicity
#          - Highest math course
#          - Field 
#      - Default is all options

# Simplify long names in survey:
# Gender identity: [cis-woman, cis-man, trans-woman, trans-man, non-bin, agender, intersex, g-fluid, other]
# Race/ethnicity: [white, black, indig-A-AK, asian, pac-isl, hisp-latx, 2+, other]
# Highest math: [alg, pre-calc, calcAB, calcBC, other]
# field: [bio, chem, phys, math, comp-sci, eng, econ, envs, bus, educ, perf-arts, vis_arts, soc-sci, eng-comm
#         phil, mod-lan, med, ear-spc, law, soc-serv]

import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
                description='Choose a search method to find a value in a list',
                prog='correlation.py')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file with survey data',
                        required=True)
    parser.add_argument('--gender_identity',
                        type=list,
                        help='The list of gender identities to examine',
                        required=False)
    parser.add_argument('--race_ethnicity',
                        type=list,
                        help='The list of race/ethnicities to examine',
                        required=False)
    parser.add_argument('--highest_math',
                        type=list,
                        help='The list of previous math experience to examine',
                        required=False)
    parser.add_argument('--field',
                        type=list,
                        help='The list of intended fields to examine',
                        required=False)

    args = parser.parse_args()
    
    # Read in the survey data file
    data = pd.read_csv(args.file_name)
    
    # filter for just demographics we are interested in
    #data_filtered = filter_data()
    
    # Find the cramers-v correlation coefficient
    #corr = cramersV(filtered_data)
    
if __name__ == '__main__':
    main()