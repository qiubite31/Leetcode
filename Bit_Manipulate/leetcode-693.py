"""
693. Binary Number with Alternating Bits
Difficulty: Easy
Related Topic: Bit Manipulate

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # print('{0:b}'.format(n))
        # print('{0:b}'.format(n>>1))
        # print('{0:b}'.format(n ^ n>>1))
        # print(n.bit_length())
        #   1 0 1 0 1 0 1 0
        # ^ 0 1 0 1 0 1 0 1
        # = 1 1 1 1 1 1 1 1
        # = pow(2, 8) -1
        if pow(2, n.bit_length())-1 == n ^ n>>1:
            return True
        else:
            return False



n = 170
solution = Solution()
output = solution.hasAlternatingBits(n)

print(output)
