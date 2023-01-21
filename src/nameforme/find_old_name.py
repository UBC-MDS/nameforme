# Authours: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 14th, 2023

def find_old_name(tp,limit=10, sex="uni", seed=None):
    """
    Generate a random set of 10(if there are that many exists) suggested neutral(by default) baby names 
    based on the given time period and sex.
    Parameters
    ----------
    tp : string, default 10
        A string specifying time period from 1880 to 2018
    limit : float
        The number of name in the output list. 
    sex : string, default "uni"
        The aimed sex of the name in the ouput. 
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
    import pandas as pd
    import numpy as np
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
    
    df = data[data["tp"]==tp]
    if sex == "uni":
        F = df[df["sex"] == 'F']["name"]
        M = df[df["sex"] == "M"]["name"]
        uni_df = list(set(F).intersection(set(M)))
        if len(uni_df) < 10:
            return uni_df
        else:
            return np.random.choice(uni_df, 10, replace=False).tolist()
    else:
        df = df[df["sex"] == sex]["name"]
        return np.random.choice(df,10,replace=False).tolist()