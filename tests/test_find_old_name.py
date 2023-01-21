# Authous: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 20th, 2023

from nameforme.nameforme import find_old_name
import pandas as pd
from numpy import sum

def test_find_old_name():
    """Test cases for find_old_name()"""

    """Test that n names are output"""
    assert len(find_old_name('1980s', limit=3)) == 3, 'The list provides different length of names'
    
    """Test that there are no duplicate names in output"""
    assert len(set(find_old_name('1980s'))) == 10, 'The defualt list is not of length 10'
    
    """Test that repeated calls generate different names"""
    first_call = find_old_name('1980s', limit=10)
    second_call = find_old_name('1980s', limit=10)
    assert set(first_call) != set(second_call), 'The list generated is not random'

    """Test that repeated calls with seed given generate same names"""
    first_call = find_old_name('1980s', seed=123)
    second_call = find_old_name('1980s', seed=123)
    assert set(first_call) != set(second_call), 'The lists generated with given seed are not the same.'
    
    """Test that name is actually of given sex"""
    URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    data = pd.read_csv(URL)
    data = data[data["sex"] == "M"]
    out = find_old_name('1980s', sex='M')
    assert sum([ _ in list(data) for _ in find_old_name('1980s', sex='M')]) == len(out), "Does not give name of right sex."