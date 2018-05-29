"""
371. Sum of Two Integers
Difficulty: Easy
Related Topic: Bit Manipulate

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        
        sum = a ^ b
        carry = (a & b) << 1
        return self.getSum(sum, carry)
        # https://leetcode.com/problems/sum-of-two-integers/discuss/84330/Python-solution-with-detailed-explanation
        # 0 0 1 0
        # 0 0 1 1
        # ^------  先將不進位的地方取xor加起來
        # 0 0 0 1 => sum

        # 0 0 1 0
        # 0 0 1 1
        # &------ 將要進位的地方取&並shfit往左進位
        # 0 0 1 0
        # <------
        # 0 1 0 0 => carry
        # 將兩個數字用recursive，直到b為0完全不需進位則回傳a
    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return(sum([a, b]))
        
a = -1
b = 1
solution = Solution()
output = solution.getSum2(a, b)

print(output)
