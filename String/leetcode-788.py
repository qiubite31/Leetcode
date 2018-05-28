"""
788. Rotated Digits
Difficulty: Easy
Related Topic: String


X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_nums = 0
        good_nums_list = []
        no_valid_nums = set(['3', '4', '7'])
        rotated_map = dict(zip('1234567890', '1534297860'))
        print(rotated_map)
        for n in range(1, N+1):
            rotated_n = ''
            for digit in str(n):
                if digit in no_valid_nums:
                    break
                else:
                    rotated_n += rotated_map[digit]

            if len(str(n)) == len(rotated_n) and not int(n) == int(rotated_n):
                good_nums_list.append(n)
                good_nums += 1

        return good_nums

N = 100
solution = Solution()
output = solution.rotatedDigits(N)

print(output)
