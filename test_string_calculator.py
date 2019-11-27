from string_calculator import add
#testing the add function
import string_calculator
def test_function_of_an_empty_string():
    assert add('') == 0

def test_function_of_one_string():
    assert add('1') == 1

def test_function_of_two_strings():
    assert add('1,2') == 3     
