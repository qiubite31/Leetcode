"""
1. Two Sum
Difficulty: Easy
Related Topic: Hash Table

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_diff_dict = {}

        for idx, num in enumerate(nums):
            num_diff_dict[target-num] = idx

        # print(num_diff_dict)
        for idx, num in enumerate(nums):
            try:
                idx2 = num_diff_dict[num]

                if idx == idx2:
                    continue
            except:
                continue

            return [idx, idx2]

nums = [3, 2, 3]
target = 6

solution = Solution()
output = solution.twoSum(nums, target)

print(output)
