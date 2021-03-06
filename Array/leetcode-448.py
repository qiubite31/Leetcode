"""
448. Find All Numbers Disappeared in an Array
Difficulty: Easy
Related Topic: Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # disapear_nums = []
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         disapear_nums.append(i)

        # return disapear_nums
        return list(set(range(1, len(nums)+1)) - set(nums))


nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
output = solution.findDisappearedNumbers(nums)

print(output)
