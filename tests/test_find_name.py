from nameforme.nameforme import find_name

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
    