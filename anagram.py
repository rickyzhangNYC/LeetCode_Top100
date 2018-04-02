'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''

def anagram(str1,str2):
    #Using a list to keep record of seen letters
    str1 = list(str1)
    for i in range(len(str2)):
        if str2[i] in str1:
            str1.remove(str2[i])
        else:
            return False
    return True

    #

str1 = 'anagram hha'
str2 = 'margana haha'

print(anagram(str1,str2))