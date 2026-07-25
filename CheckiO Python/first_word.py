"""
You are given a string and you have to find its first word.

    The input string consists of only English letters and spaces.
    There aren’t any spaces at the beginning and the end of the string.

example

Input: A string (str).

Output: A string (str). 
"""
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]

# OR THIS
"""
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]

"""
