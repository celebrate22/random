"""
 In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same - your function should return False.

example

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first, and the third is a symbol (str) that should go after the first one.

Output: A logic value (bool). 
"""

def goes_after(word: str, first: str, second: str) -> bool:
    # Rule: If two seeking symbols are the same, return False
    if first == second:
        return False
    
    # Loop up to the second-to-last character index
    for i in range(len(word)-1):
        # Check if current character matches 'first' AND the next matches 'second'
        if word[i] == first and word[i + 1] == second:
            return True
            
    return False


print("Example:")
print(goes_after("world", "w", "o"))
print(goes_after("world", "w", "o"))
print(goes_after("world", "w", "r"))
print(goes_after("world", "l", "o"))
print(goes_after("list", "l", "o"))
print(goes_after("", "l", "o"))
print(goes_after("list", "l", "l"))
print(goes_after("world", "d", "w"))


