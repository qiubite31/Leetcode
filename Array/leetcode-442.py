"""
442. Find All Duplicates in an Array
Difficulty: Medium
Related Topic: Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                nums[i] = nums[i] - nums[i]
                break

            if not nums[i] == nums[i+1]:
                nums[i] = nums[i] - nums[i]
                i += 1
            else:
                nums[i+1] = nums[i+1] - nums[i+1]
                i += 2

        return [num for num in nums if not num == 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
output = solution.findDuplicates(nums)

print(output)
