# Authours: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 14th, 2023

import pandas as pd
import numpy as np

def find_unisex_name(bar,limit=10):
    """
    Generate the a random set of 10 suggested neutral baby names 
    based on the given limitation and baby names in the past years.
    Parameters
    ----------
    limit : float
        A float controls the minimum proportion of the neutral names in a single year in the dataframe.
    count : integer
        The length of the output with a default value of 10
    Returns
    -------
    list:
        A word list containing random suggested neutral names based on the given limitation
        If the length of the word list is less than the limitation, it will return all the names in the word list
    Examples
    --------
    >>> limit=0.0001
    >>> find_unisex_name(limit)
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    #check input value
    if not (bar > 0 and bar < 1):
        raise Exception("bar value should within 0 and 1")
    
    # Load data
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    data = pd.read_csv(url)
    
    # data wrangling
    bar_data_boy = data[(data['prop'] > bar) & (df['sex'] == 'M')] # select all the boy names with prop greater than bar
    bar_data_girl = data[(data['prop'] > bar) & (df['sex'] == 'F')] # select all the girl names with prop greater than bar
    target_names = []
    for girl_name in set(bar_data_girl['name']):
        if girl_name in set(bar_data_boy['name']):
            target_names.append(girl_name)
    
    # Create name list
    if len(target_names) = 0:
        raise Exception("Please lower the bar value")
    if len(target_names) < limit:
        result = target_names
    else:
        result = np.random.choice(target_names, limit, replace=False).tolist()
    
    return result