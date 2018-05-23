"""
485. Max Consecutive Ones
Difficulty: Easy
Related Topic: Array


Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cons_one = 0
        cons_one = 0
        for num in nums:
            if num == 1:
                cons_one += 1
            else:
                if max_cons_one < cons_one:
                    max_cons_one = cons_one
                cons_one = 0

        return max(max_cons_one, cons_one)

    def findMaxConsecutiveOnes2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_str = ''.join([str(num) for num in nums])
        return max([len(cons_one) for cons_one in nums_str.split('0')])


nums = [1, 1, 0, 1, 1, 1]
solution = Solution()
output = solution.findMaxConsecutiveOnes2(nums)

print(output)
