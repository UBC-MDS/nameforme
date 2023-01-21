# Authous: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 21st, 2023

from nameforme.nameforme import find_name
import pandas as pd
from numpy import sum

def test_find_unisex_name():
    """Test cases for find_unisex_name()"""
    
    """Test that the characters in the output are all alphabetic"""
    assert sum(str.isalpha(i) for i in find_unisex_name(bar=0.02,limit=10)) == 10, 'The output is illegal'
    
    """Test that the length of the output is correct"""
    assert len(find_unisex_name(bar=0.02,limit=5)) == 5, 'The list does not provide the correct length of names'
    
    """Test that no duplicate names are found in the output"""
    assert len(set(find_unisex_name(bar=0.02,limit=10))) == 10, 'The length of the output is not correct'
    
    """Test that changing bar value create new name list"""
    assert set(find_unisex_name(bar=0.02,limit=10)) != set(find_unisex_name(bar=0.01,limit=10)), 'The output of different bar value should not be the same '
    
    """Test that the prop of first output name are higher than the bar value"""
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    data = pd.read_csv(url)
    names = find_unisex_name(bar=0.02,limit=5)
    assert data[data['name']==names[0]]['prop'][0] > 0.02 == True, "The output's prop value should not be smaller than the bar"
    