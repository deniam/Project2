"""
Name of the function: count words
Argument: string
Returns: number of the words
Build-in functions to use: len()
Methods to use: .split()
"""
from lib.count_words import *

def test_length_of_the_string():
    result = count_words("It will be sunny day tomorrow and rain on day after tomorrow.")
    assert result == 12

def test_length_of_the_empty_string():
    result = count_words("")
    assert result == 0