# Authours: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 14th, 2023

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