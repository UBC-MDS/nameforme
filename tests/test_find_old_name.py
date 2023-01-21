# Authous: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 20th, 2023

from nameforme.nameforme import find_old_name

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