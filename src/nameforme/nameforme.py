def find_unisex_name(limit=0.2):
    """
    Generate the a random set of 10 suggested neutral baby names 
    based on the given limitation and baby names in the past years.
    Parameters
    ----------
    limit : float
        A float controls the minimum proportion of the neutral names in a single year in the dataframe. 
    Returns
    -------
    list:
        A word list containing random 10 suggested neutral names based on the given limitation
    Examples
    --------
    >>> limit=0.0001
    >>> find_unisex_name(limit)
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    pass

def find_old_name(tp,limit=10, sex="uni"):
    """
    Generate the a random set of 10 suggested neutral(by default) baby names 
    based on the given time period and sex.
    Parameters
    ----------
    tp : string, default 10
        A string specifying time period from 1880 to 2018
    limit : float
        The number of name in the output list. 
    sex : string, default "uni"
        The aimed sex of the name in the ouput. 
    Returns
    -------
    list:
        A name list containing random suggested old names based on the given limitation.
    Examples
    --------
    >>> find_old_name('80s')
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    pass

def find_similar_name(name, limit=10):
    """
    Generate the a random set of 10 suggested similar baby names 
    based on the syllable of the input name. 
    Parameters
    ----------
    name : string
        the given name used to find similar names based on syllable. 
    limit : float
        The number of name in the output list.  
    Returns
    -------
    list:
        A name list containing random suggested similar names based on the given name.
    Examples
    --------
    >>> find_old_name('Rowan')
    >>> ['Skylar', 'Azariah', 'Royal', 'Hayden', 'Emerson', 'Rowan', 'Baylor', 'Dakota', 'River', 'Emory']
    """
    pass

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
    >>> find_name('boy', 'A', 3)
    >>> ['Aiden', 'Aaron', 'Asher','Angel','Adam']
    """
    pass