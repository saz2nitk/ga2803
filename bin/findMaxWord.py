# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:30:01 2021

@author: saz2n
"""

"""
Given a list of words, find the largest word not greater than length 5
"""

list_words = ['good', 0, 'ram', 1.1, 'apple', 'abrakadabra', 'cat', 'mango']


def lessthan_x(input_string, max_len=5):
    """
    lessthan_x function
    returns True if length of input_string is less than or equal to max_len
    else returns False
    """
    if len(input_string) <= max_len:
        return True
    return False

try:
    max_len_word = max(filter(lessthan_x, list_words), key=len)
except TypeError:
    print("Please pass string in list_words")

print("The max len word less is :", max_len_word)
