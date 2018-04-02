'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''

def anagram(str1,str2):
    #Using a list to keep record of seen letters
    str1 = list(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] in str1:
                str1.remove(str2[j])
    if not str1:
        return True
    else:
        return False

str1 = 'anagram'
str2 = 'margana'

print(anagram(str1,str2))