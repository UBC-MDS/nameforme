def find_unisex_name(data,limit):
    """
    Generate the a random set of 10 suggested neutral baby names 
    based on the given limitation and baby names in the past years.
    Parameters
    ----------
    data : Pandas DataFrame
        A csv file containing baby names from 1880 to 2018
    limit : float
        A float controls the minimum proportion of the neutral names in a single year in the dataframe. 
    Returns
    -------
    list:
        A word list containing random 10 suggested neutral names based on the given limitation
    Examples
    --------
    >>> dat=pd.read_csv('babyname.csv')
    >>> limit=0.0001
    >>> find_unisex_name(dat,limit)
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    pass