"""
796. Rotate String
Difficulty: Easy
Related Topic: String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == 0 and len(B) == 0:
            return True

        for i in range(len(A)):
            if A[i+1:] + A[0:i+1] == B:
                return True

        return False

A = 'abcde'
B = 'cdeab'
solution = Solution()
output = solution.rotateString(A, B)

print(output)