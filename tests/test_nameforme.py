from nameforme.nameforme import find_name
from nameforme.nameforme import find_old_name
from nameforme.nameforme import find_similar_name
from nameforme.nameforme import find_unisex_name

import pandas as pd
import jellyfish as jf
import random
import pytest


def test_find_name():
    """Test cases for find_name()"""
    
    """Test that the names are in the same length"""
    assert len(set(len(i) for i in find_name("F", "A", 3))) == 1, 'The list provides different length of names'
    
    """Test that the names match the required length"""
    assert next(iter(set(len(i) for i in find_name("F", "A", 3)))) == 3, 'The list does not provide the correct length of names'
    
    """Test that the names are start with the same letter"""
    assert len(set(i[0] for i in find_name("F", "A", 3))) == 1, 'The list provides different initial letter of names'
    
    """Test that the names match the required initial letter"""
    assert next(iter(set(i[0] for i in find_name("F", "A", 3)))) == 'A', 'The list does not provide the correct initial letter of names '
    
    """Test that there are no duplicate names in output"""
    assert len(set(find_name("F", "A", 3))) == len(find_name("F", "A", 3)), 'The list should not have duplicated names'
    

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
    
def test_find_similar_name():
    """Test cases for find_similar_name()"""

    """Test that n names are output"""
    assert len(find_similar_name('Daniel', limit=3)) == 3, "Wrong number of names output"
    
    """Test that there are no duplicate names in output"""
    assert len(set(find_similar_name('Daniel'))) == 10, "Duplicate names in the output"
    
    """Test that repeated calls generate different names"""
    first_call = find_similar_name('Daniel', limit=20)
    second_call = find_similar_name('Daniel', limit=20)
    assert set(first_call) != set(second_call), "Sucessive calls don't seem random"

    """Crude similarity test: checking if first letter matches"""
    assert "D" in [name[0] for name in find_similar_name('Daniel', 3)], "Doesn't seem like the generated names are similar"
        
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
    
    