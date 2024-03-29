import pytest
from string_calculator import add
#testing the add function
import string_calculator
def test_function_of_an_empty_string():
    assert add('') == 0

def test_function_of_one_string():
    assert add('1') == 1

def test_function_of_two_strings():
    assert add('1,2') == 3   

def test_function_of_delimeters():
    assert add('1\n2,3') == 6

def test_function_of_negatives():
    with pytest.raises(ValueError) as VE:
        add('-5,-4')
    assert "negatives" in str(VE.value)
def test_function_of_number_greater_than_1000():
    assert add('2,1001')

def test_function_of_lengthy_delimeters():
    assert add('//[***]\n1***2***3') == 6  

def test_function_of_multiple_delimeters():
    assert add('//[*][%]\n1*2%3') == 6   

     


