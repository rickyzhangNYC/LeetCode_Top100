import sys
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# class Solution:
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    #Doesn't work because it should maintain order
    # ptr1 = 0
    # ptr2 = len(nums)-1
    
    # while (ptr1<ptr2):
    #     print('ptr1:',ptr1)
    #     print('ptr2:',ptr2)
    #     if nums[ptr1] == 0:
    #         nums[ptr1] = nums[ptr2]
    #         nums[ptr2] = 0
    #         ptr2 -= 1
    #     ptr1 += 1

    swapWithZero = 0
    for n in range(len(nums)):
        # Hard to do with ==0 because at end of list, there will all be zeroes, can maybe implement going backwards
        if nums[n] != 0:
            nums[n],nums[swapWithZero] = nums[swapWithZero],nums[n]
            swapWithZero += 1

a = [0, 1, 0, 3, 12]
moveZeroes(a)
print(a)