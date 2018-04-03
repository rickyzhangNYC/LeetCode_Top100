'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

'''

def containsDuplicate(arr):
    # Create dictionary and input all keys into dictionary. Increment values and check values for > 1.
    intdict = dict()
    for i in arr:
        # If key not in dict, store.
        if i not in intdict:
            intdict[i] = 1
        # Else, increment
        else:
            intdict[i] += 1
    # Check each value, if > 1 return True, else False
    for v in intdict.values():
        if v > 1 :
            return True
    return False

arr = [1,23,5,4,21,4,1,2,1]

print(containsDuplicate(arr))