# Authous: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 16th, 2023

from nameforme.nameforme import find_similar_name

def test_find_similar_name():
    """Test cases for find_similar_name()"""

    """Test that n names are output"""
    assert len(find_similar_name('Daniel', limit=3)) == 3
    
    """Test that there are no duplicate names in output"""
    assert len(set(find_similar_name('Daniel'))) == 10
    
    """Test that repeated calls generate different names"""
    first_call = find_similar_name('Daniel', limit=20)
    second_call = find_similar_name('Daniel', limit=20)
    assert set(first_call) != set(second_call)

    """Crude similarity test: checking if first letter matches"""
    assert "D" in [name[0] for name in find_similar_name('Daniel', 3)]
    
