"""
461. Hamming Distance
Difficulty: Easy
Related Topic: Bit Manipulation, XOR 

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = x ^ y
        return len("{0:b}".format(result).replace('0',''))

x = 1
y = 4
solution = Solution()
output = solution.hammingDistance(x, y)

print(output)
