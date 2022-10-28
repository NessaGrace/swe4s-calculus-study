# Goal: given a csv file of survey responses, find the probability 
# that that demographic will take calc 2 in the future

import argparse
import pandas as pd
import utils
import viz_lib
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(
                description='Find correlations for calculus 2 retention',
                prog='probability.py')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file with survey data',
                        required=True)
    parser.add_argument('--gender_identity',
                        nargs='+',
                        help='The list of gender identities to examine',
                        required=False)
    parser.add_argument('--race_ethnicity',
                        nargs='+',
                        help='The list of race/ethnicities to examine',
                        required=False)
    parser.add_argument('--highest_math',
                        nargs='+',
                        help='The list of previous math experience to examine',
                        required=False)
    parser.add_argument('--field',
                        nargs='+',
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
    filtered_gender = utils.filter_data(
      data, 
      'gender_id', 
      args.gender_identity)
    
    # Then filter race/ethnicity
    filtered_gender_race = utils.filter_data(
       filtered_gender, 
       'race_eth', 
       args.race_ethnicity)
    
    # Make sure filtered data is non-empty
    if len(filtered_gender_race.index) == 0:
        raise KeyError("Sorry, no survey responses match this request. " +
                       "Please try again with a broader search.")
        sys.exit(1)
                       
    # Warn user if there are less than 30 responses
    if len(filtered_gender_race.index) <= 30:
        print("Warning: there are very few students that match your " +
              "inquiry. Results may not be accurate.\nNumber of " + 
              f"responses: {len(filtered_gender_race.index)}")
    
    # Find the probability to take calc 2
    all_probs = utils.find_probs(data, "calc2")['Yes']

    # Make sure there is at least 1 yes response
    if 'Yes' in filtered_gender_race.calc2:
        filt_probs = utils.find_probs(filtered_gender_race, "calc2")['Yes']
    else:
        filt_probs = 0

    # Compare to women and men statisitcs
    women_filt = utils.filter_data(data, 'gender_id', ['cis_W', 'trans_W'])
    women_probs = utils.find_probs(women_filt, 'calc2')['Yes']
    
    men_filt = utils.filter_data(data, 'gender_id', ['cis_M', 'trans_M'])
    men_probs = utils.find_probs(men_filt, 'calc2')['Yes']
    
    # create a bar chart with identity on x-axis and probability on the y-axis
    labels = ['Input student', 'All students', 'Women', 'Men']
    probs = [filt_probs, all_probs, women_probs, men_probs]
    viz_lib.bar(x=labels,
                y=probs,
                title="Probabilities of a student taking Calculus II",
                xlabel="Demographic",
                ylabel="Probability to take Calculus II",
                file_name="probabilities_bar.png")

if __name__ == '__main__':
    main()