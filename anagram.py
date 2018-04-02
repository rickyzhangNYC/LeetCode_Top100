'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''

def anagram(s,t):
    # #Using a list to keep record of seen letters
    # #Time Complexity O(n^2)
    # #Space O(1)
    # s = list(s)
    # for i in range(len(t)):
    #     if t[i] in s:
    #         s.remove(t[i])
    #     else:
    #         return False
    # return True

    #Using a hash table to keep a counter
    charDict = dict()
    for i in s:
        if i not in charDict:
            charDict[i] = 1
        else:
            charDict[i] += 1

    for j in t:
        if j not in charDict:
            return False
        else:
            charDict[j] -= 1
    for v in charDict.values():
        if v != 0:
            return False
    return True

s = 'anagram hhaa'
t = 'margana haah'

print(anagram(s,t))