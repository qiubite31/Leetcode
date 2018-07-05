"""
169. Majority Element
Difficulty: Easy
Related Topic: Array

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        threshold = math.floor(len(nums)/2)
        
        num_dict = {}
        max_count = -1
        for num in nums:
            try:
                num_dict[num] = num_dict[num] + 1
            except:
                num_dict[num] = 1
            
            if num_dict[num] > threshold:
                return num


nums = [2,2,1,1,1,2,2]
solution = Solution()
output = solution.majorityElement(nums)

print(output)
