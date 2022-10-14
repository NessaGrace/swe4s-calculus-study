''' Functions to aid in the survey analysis

    * cramersV - Finds the Cramers-V correlation coefficient

'''

import pandas as pd


def cramersV():
    '''
    Calculate the Cramers-V correlation coefficient for categorical data
    
    Parameters
    ----------
    
    Returns
    -------
    
    '''
    return -1

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
    filtered_data : A pandas dataframe with only the desired keys in the column.
    
    '''
    # make sure data is a dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data input must be pandas dataframe")
        
    # make sure col_name is actually a column name
    if not col_name in data.columns:
        raise KeyError("col_name not a column in data")
    
    filtered_data = data[data[col_name].isin(keys)]
    
    return filtered_data