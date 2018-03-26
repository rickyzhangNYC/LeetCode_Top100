"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
import sys

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    #Hint: Changing from base 10 to base 26 because each letter will correspond to a digits place
    #Reverse string
    total = 0
    s = s[::-1]
    #Loop through string and multiply the value of the letter by its converted base and add it to a total count
    for i in range(len(s)):
        num = ord(s[i]) - 64
        digit = 26**i
        total += num*digit
    return total

print(titleToNumber('BA'))