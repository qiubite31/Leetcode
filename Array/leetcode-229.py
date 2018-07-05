"""
229. Majority Element II
Difficulty: Medium
Related Topic: Array

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        threshold = int(len(nums)/3)
        
        num_dict = {}
        majority_num = []
        
        for num in nums:
            try:
                num_dict[num] = num_dict[num] +1
            except:
                num_dict[num] = 0
                
            if num_dict[num] >= threshold:
                majority_num.append(num)
                
        return list(set(majority_num))


nums = [2,2,1,1,1,2,2]
solution = Solution()
output = solution.majorityElement(nums)

print(output)
