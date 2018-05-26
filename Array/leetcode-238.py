"""
283. Move Zeroes
Difficulty: Easy
Related Topic: Array, Two Pointers

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_loc = []
        for idx, n in enumerate(nums):
            if n == 0:
                zero_loc.append(idx)

        for loc in zero_loc[::-1]:
            del nums[loc]
            nums.append(0)
    
        return nums
    
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_loc = 0
        for idx, n in enumerate(nums):
            if not n == 0:
                nums[zero_loc], nums[idx] = nums[idx], nums[zero_loc]
                zero_loc += 1

    
        return nums


nums = [0, 1, 0, 3, 12]
solution = Solution()
output = solution.moveZeroes2(nums)

print(output)
