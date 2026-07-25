"""
Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative" or "zero".

example

Input: Integer (int).

Output: String (str). 
"""

def determine_sign(num: int) -> str:
    if num == 0: return 'zero'
    if num > 0: return 'positive'
    return 'negative'