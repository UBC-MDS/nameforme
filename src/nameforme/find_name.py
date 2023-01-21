import pandas as pd
import random

def find_name(sex, init, length):
    """
    Generate the a random set of 10 suggested baby names based on the given limitations.
    Parameters
    ----------
    sex: string, 
        The sex of baby's name, either 'F' or 'M' or 'f' or 'm'
    init : string
        The initial of baby's name, a single character
    length : int
        The length of baby's name 
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
        raise TypeError("sex needs to be of str type.")
    
    # Check input type of init
    if not isinstance(init, str):
        raise TypeError("init needs to be of str type.")

    # Check input type of length
    if not isinstance(length, int):
        raise TypeError("length needs to be of int type.")
    
    # Check input value of sex
    if not (sex == 'F' or sex == 'M' or sex == 'f' or sex == 'm'):
        raise Exception("sex should be either 'F/f' or 'M/m'")
    
    # Check input value of init
    if not (len(init) == 1):
        raise Exception("init should be a single character")
    
    if not (str.isalpha(init)):
        raise Exception("init should be an alphabet")
    
    # Check input value of length
    if length <= 0:
        raise Exception("length should be larger than 0")
    
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