# Authours: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 14th, 2023

import pandas as pd
import numpy as np
import jellyfish as jf
import random

def find_name(sex, init, length):
    """
    Generate the a random set of 10 suggested baby names based on the given limitations.
    Parameters
    ----------
    sex: string, 
        The sex of baby's name, either 'F' or 'M' or 'f' or 'm'
    init : string
        The initial of baby's name, a single alphabet character
    length : int
        The length of baby's name, larager than 0
    Returns
    -------
    list:
        A name list containing random suggested names based on the given limitation.
    Examples
    --------
    >>> find_name('F', 'A', 3)
    >>> ['Ada', 'Aja', 'Ani', 'Aya', 'Ava', 'Ana', 'Ari', 'Ali', 'Ami', 'Amy']
    """
    # Check input type of sex
    if not isinstance(sex, str):
        raise TypeError("sex needs to be a str type.")
    
    # Check input type of init
    if not isinstance(init, str):
        raise TypeError("init needs to be a str type.")

    # Check input type of length
    if not isinstance(length, int):
        raise TypeError("length needs to be an int type.")
    
    # Check input value of sex
    if not (sex == 'F' or sex == 'M' or sex == 'f' or sex == 'm'):
        raise Exception("sex should be either 'F'/'f' or 'M'/'m'.")
    
    # Check input value of init
    if not (len(init) == 1):
        raise Exception("init should be a single character.")
    
    if not (str.isalpha(init)):
        raise Exception("init should be an alphabet.")
    
    # Check input value of length
    if length <= 0:
        raise Exception("length should be larger than 0.")
    
    # Data loading and cleaning   
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    raw_df = pd.read_csv(url)
    raw_df = raw_df[raw_df['n'] >= 100] # Keep only names that had at least 100 births for a single gender in a single year
    
    # Filter data based on the arguments
    df_sex = raw_df.loc[raw_df['sex'] == sex.capitalize()]
    df_init = df_sex.loc[df_sex['name'].str.startswith(init.capitalize(), na=False)]
    df_len = df_init.loc[df_init['name'].str.len() == length]
    
    # Create name list and randomly select 10 names
    name_list = df_len['name'].unique().tolist()
    if len(name_list) < 10:
        sampled = random.sample(name_list, k=len(name_list))
    else:
        sampled = random.sample(name_list, k=10)    
    
    return sampled


def find_old_name(tp,limit=10, sex="uni", seed=None):
    """
    Generate a random set of 10(if there are that many exists) suggested neutral(by default) baby names 
    based on the given time period and sex.
    Parameters
    ----------
    tp : string, default 10
        A string specifying time period from 1880 to 2018
        List of possible qualified inputs:
        ['1880s','1890s','1900s','1910s','1920s','1930s','1940s','1950s','1960s','1970s','1980s','1990s','2000s','2010s']
    limit : float
        The number of name in the output list. 
    sex : string, default "uni"
        The aimed sex of the name in the ouput.
        List of possible qualified inputs:
        ["uni","M","F] 
    seed : int
        if provided, returns the same random set. 
    Returns
    -------
    list:
        A name list containing random suggested old names based on the given limitation.
    Examples
    --------
    >>> find_old_name('1980s', seed=123)
    >>> ['Neng','Rashida','Krister','Garry','Kai','Chezare','Dolores','Tyler','Skylar','Tyrie']
    """
    # Load data
    URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    data = pd.read_csv(URL)
    # Data wrangling
    data["tp"] = np.select(
        [
            data["year"].between(1880,1890, inclusive="left"),
            data["year"].between(1890,1900, inclusive="left"),
            data["year"].between(1900,1910, inclusive="left"),
            data["year"].between(1910,1920, inclusive="left"),
            data["year"].between(1920,1930, inclusive="left"),
            data["year"].between(1930,1940, inclusive="left"),
            data["year"].between(1940,1950, inclusive="left"),
            data["year"].between(1950,1960, inclusive="left"),
            data["year"].between(1960,1970, inclusive="left"),
            data["year"].between(1970,1980, inclusive="left"),
            data["year"].between(1980,1990, inclusive="left"),
            data["year"].between(1990,2000, inclusive="left"),
            data["year"].between(2000,2010, inclusive="left"),
            data["year"].between(2010,2020, inclusive="left"),
        ],
        [
            '1880s',
            '1890s',
            '1900s',
            '1910s',
            '1920s',
            '1930s',
            '1940s',
            '1950s',
            '1960s',
            '1970s',
            '1980s',
            '1990s',
            '2000s',
            '2010s'
        ]
    )
    # Setting seed.
    if seed is not None:
        np.random.seed(seed)
    if tp not in ['1880s','1890s','1900s','1910s','1920s','1930s','1940s','1950s','1960s','1970s','1980s','1990s','2000s','2010s'] or sex not in ["uni",'M','F']:
        raise Exception("Sorry, please enter valid time periods/sex!")
    
    df = data[data["tp"]==tp]
    if sex == "uni":
        F = df[df["sex"] == 'F']["name"]
        M = df[df["sex"] == "M"]["name"]
        uni_df = list(set(F).intersection(set(M)))
        if len(uni_df) < 10:
            return uni_df
        else:
            return np.random.choice(uni_df, limit, replace=False).tolist()
    else: 
        df = df[df["sex"] == sex]["name"]
        return np.random.choice(df,limit,replace=False).tolist()
    

def find_similar_name(match_name, limit=10):
    """
    Generate a random list of names that sound similar to a given user input name.
    
    Uses Match rating approach algorithm to determine similarity
      
    Parameters
    ----------
    match_name : string
        Name for comparison; output names will sound like this one 
    limit : int
        The number of names in the output list. (default = 10)
    Returns
    -------
    list:
        A name list containing random suggested similar names based on the given name.
    Examples
    --------
    >>> find_similar_name('Elizabeth', 5)
    >>> ['Elisabeth', 'Elliott', 'Ellsworth', 'Emmalynn', 'Ryley']
    """
    
    # Check inputs
    if not isinstance(match_name, str):
        raise TypeError("input name must be a string")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    
    # Data loading and cleaning
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    raw_df = pd.read_csv(url)
    raw_df = raw_df[raw_df["n"] >= 100] # Keep only names that had at least 100 births for a single gender in a single year
    unique_names = raw_df['name'].unique()
    unique_names = unique_names[unique_names != match_name] # Remove target name from potential outputs
    
    # Calculate targets 
    encodings = [jf.match_rating_codex(n) for n in unique_names]
    target = jf.match_rating_codex(match_name)
    distance = [jf.jaro_winkler_similarity(target, e) for e in encodings]
    
    df = pd.DataFrame(data = [unique_names, encodings, distance]).T
    df.columns = ["name", "encoding", "match_score"]
    df["weight"] = (df["match_score"]*2)**10 # Heavily weigh higher scores
    
    # Sample n names to output, weighted by match_score
    sampled = df.sample(n = limit, weights = "weight")
    sampled = sampled.sort_values(by = "match_score", ascending = False)
    return(sampled["name"].to_list())

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
    >>> limit=10
    >>> find_unisex_name(0.2,limit)
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    
    #check input value
    if not (bar > 0 and bar < 1):
        raise Exception("bar value should within 0 and 1")
    
    # Load data
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    data = pd.read_csv(url)
    
    # data wrangling
    bar_data_boy = data[(data['prop'] > bar) & (data['sex'] == 'M')] # select all the boy names with prop greater than bar
    bar_data_girl = data[(data['prop'] > bar) & (data['sex'] == 'F')] # select all the girl names with prop greater than bar
    target_names = []
    for girl_name in set(bar_data_girl['name']):
        if girl_name in set(bar_data_boy['name']):
            target_names.append(girl_name)
    
    # Create name list
    common_unisex_names=['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 
                         'Rowan', 'Baylor', 'Dakota', 'River', 'Emory','Jessie',
                         'Marion','Jackie','Alva','Ollie','Jodie','Cleo','Kerry']
    if len(target_names) < limit:
        result = target_names + np.random.choice(common_unisex_names, limit-len(target_names), replace=False).tolist()
    else:
        result = np.random.choice(target_names, limit, replace=False).tolist()
    
    return result