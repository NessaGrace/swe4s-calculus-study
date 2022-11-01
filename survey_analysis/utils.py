''' Functions to aid in the survey analysis

    * filter_data - Filters dataframe for target column values
    * find_probs - Find probability of each unique column value occurring
'''

import pandas as pd
import numpy as np


def filter_data(data, col_name, keys):
    '''
    Filter data to only include specified keys in a given column

    Parameters
    ----------
    data : Dataset that needs filtering. Expects .pandas dataframe.

    col_name : The name of the column to look for keys in. Expects a string.

    keys : Values in the column to filter for.

    Returns
    -------
    filtered_data : A dataframe with only the desired keys in the column

    '''
    # make sure data is a dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data input must be pandas dataframe")

    # make sure col_name is actually a column name
    if col_name not in data.columns:
        raise KeyError("col_name not a column in data")

    # make sure keys is a list
    if not isinstance(keys, list):
        raise TypeError("keys must be type list")

    # filter the data
    filtered_data = data[data[col_name].isin(keys)]

    return filtered_data


def find_probs(data, col_name):
    '''
    Find probability of each unique value in a given column

    Parameters
    ----------
    data : Dataset that needs filtering. Expects pandas dataframe.

    col_name : The name of the column to look for keys in. Expects a string.

    Returns
    -------
    prob_dict = A dictionary of probabilities for each value in the column

    '''
    # Select column
    col = data[col_name]

    # Values in column
    vals = col.value_counts().index.tolist()

    # Find number of counts for each value
    counts = []
    for i in range(len(vals)):
        counts.append(col.value_counts()[i])
    counts = np.array(counts)

    # Find the probabilities for each value using counts
    probs = []
    sum_ = counts.sum()
    for i in range(len(vals)):
        probs.append(counts[i]/sum_)
    probs = np.array(probs)

    # create a dictionary of values and probabilities
    prob_dict = dict(zip(vals, np.round(probs, 3)))

    return prob_dict
