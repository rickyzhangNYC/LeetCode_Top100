"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
"""
def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """ 
    # Personal try
    # counter = 0
    # i = 0
    # position = (i+k)%len(nums)
    # temp = nums[position]
    # nums[position] = nums[i]
    # nums[i]= None
    # while counter != len(nums)-1:
    #     i = position
    #     position = (i+k)%len(nums)
    #     if position == 0 :
    #         nums[position] = temp
    #     else:
    #         nums[position],temp = temp,nums[position]
    #     counter += 1


    # Classic approach, 3 step array rotation
    # 1 reverse the first n - k elements
    # 2 reverse the rest of them
    # 3 reverse the entire array

    # def rotate(self, nums, k):
    #     if k is None or k <= 0:
    #         return
    #     k, end = k % len(nums), len(nums) - 1
    #     self.reverse(nums, 0, end - k)
    #     self.reverse(nums, end - k + 1, end)
    #     self.reverse(nums, 0, end)
        
    # def reverse(self, nums, start, end):
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start, end = start + 1, end - 1

    # Iterative approach
    # put the last k elements in correct position (ahead) and do the remaining n - k. Once finish swap, the n and k decrease.
    # n, k, j = len(nums), k % len(nums), 0
    # while n > 0 and k % n != 0:
    #     for i in range(0, k):
    #         nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
    #     n, j = n - k, j + k
    #     k = k % n
    

a = [1,2,3,4,5,6]

rotate(a,2)

print(a)