# ChatGPT Python Exercises Intermediate

"""
Write a Python function that takes a list of strings as input and 
returns a new list containing only the strings that are palindromes 
(read the same forwards and backwards).
"""

def return_palindrome(list_of_strings):
    list_of_palindrome = []
    for i in list_of_strings:
        reversed_string = i[::-1]
        if i.lower() == reversed_string.lower(): 
            list_of_palindrome.append(i)
    return list_of_palindrome

"""
Write a Python function that takes a list of words as input and returns
a dictionary where the keys are the words and the values are the 
lengths of the corresponding words.
"""

def return_dictionary(list_of_words):
    dictionary = {}
    for string in list_of_words:
        dictionary[string] = len(string)
    return dictionary
