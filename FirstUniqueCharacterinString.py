'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Note: You may assume the string contain only lowercase letters.
'''

def firstUniqChar(s):
    queue = list()
    indexdict = dict()
    for i in range(len(s)):
        if s[i] not in indexdict:
            indexdict[s[i]] = i
            queue.append(s[i])
        else:
            del indexdict[s[i]]
            queue.remove(s[i])
        # elif queue[0] == s[i]:
        #     del indexdict[s[i]]
        #     queue.pop(0)
        # else:
        #     del indexdict[s[i]]
        #     queue.append(s[i])
    if indexdict[queue[0]] != 1:
        return indexdict[queue[0]]
    else:
        return -1

s = "aadadaad"

print(firstUniqChar(s))