import pandas as pd
import random

def find_name(sex, init, len):
    """
    Generate the a random set of 10 suggested baby names based on the given limitations.
    Parameters
    ----------
    sex: string, 
        The sex of baby's name 
    init : string
        The initial of baby's name
    len : int
        The length of baby's name 
    Returns
    -------
    list:
        A name list containing random suggested names based on the given limitation.
    Examples
    --------
    >>> find_name('F', 'A', 3)
    >>> ['Ami', 'Ana', 'Ada', 'Ana', 'Ava', 'Aya', 'Aja', 'Ani', 'Ada', 'Ani']
    """
    # Data loading and cleaning   
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    raw_df = pd.read_csv(url)
    raw_df = raw_df[raw_df['n'] >= 100] # Keep only names that had at least 100 births for a single gender in a single year
    
    # Filter data based on the arguments
    df_sex = raw_df.loc[raw_df['sex']==sex]
    df_init = df_sex.loc[df_sex['name'].str.startswith(init, na=False)]
    df_len = df_init.loc[df_init['name'].str.len() == 3]
    
    # Create name list and randomly select 10 names
    name_list = df_len['name'].unique()
    sampled = random.choices(name_list, k=10)    
    
    return sampled