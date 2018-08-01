"""
258. Add Digits
Difficulty: Easy
Related Topic: Math, Digital root


Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:
            num = sum([int(digit) for digit in str(num)])
            # sum(list(map(int, str(num))))

        return num

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        import math
        return num - 9 * math.floor((num-1)/9)

num = 38
solution = Solution()
output = solution.addDigits2(num)

print(output)
