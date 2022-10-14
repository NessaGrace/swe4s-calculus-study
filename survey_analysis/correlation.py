# Goal: given a csv file of survey responses, find the correlation 
# that that demographic has to taking calc 2 in the future

import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
                description='Find correlations for calculus 2 retention',
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
    
    # Rename columns so they are easier to read and work with
    data = data.set_axis(
        ['gender_id', 'race_eth', 'hmath', 'field', 'calc2', 'reason'], 
        axis=1)
    
    # Create dictionaries to shorten responses in the dataframe
    gen_dict = {
        '"Cis-gender woman (female at birth, identify as a woman)"': 'cis_W',      
        '"Cis-gender man (male at birth, identify as a man)"': 'cis_M',
        '"Transgender woman (male at birth, identify as a woman)"': 'trans_W',
        '"Transgender man (female at birth, identify as a man)"': 'trans_M',
        "Non-binary / genderqueer (don't identify exclusively as a man or a woman)": 'non_binary',
        "Agender (don't identify as any gender)": 'agender',
        'Intersex (have a combination of male and female biological traits)':'intersex',
        'Gender fluid (gender identity and/or expression varies over time)': 'gender_fluid',
        'Other:': 'other'}

    race_dict = {
        'White (non-Hispanic/Latinx)': 'white',
         'Black/African American (non-Hispanic/Latinx)': 'black',
         'Indigenous/Native American/Native Alaskan (non-Hispanic/Latinx)': 'native_amer_AK',
         'Asian/Asian American (non-Hispanic/Latinx)': 'asian',
         'Native Hawaiian/Pacific Islander (non-Hispanic/Latinx)': 'pacific_isl',
         'Hispanic/Latinx': 'hisp_latx',
         '2 or more races': '2+',
         'Other:': 'other'}
    
    # Use dictionaries to shorten the responses
    data['gender_id'] = data['gender_id'].map(gen_dict)
    data['race_eth'] = data['race_eth'].map(race_dict)
    
    # filter for just demographics we are interested in
    # First filter gender identity
    filtered_gender = filter_data(
      data, 
      'gender_id', 
      args.gender_identity)
    
    # Then filter race/ethnicity
    filtered_gender_race = filter_data(
       filtered_gender, 
       'race_eth', 
       args.race_ethnicity)
    
    # Find the cramers-v correlation coefficient
    #corr = cramersV(filtered_data)
    
if __name__ == '__main__':
    main()