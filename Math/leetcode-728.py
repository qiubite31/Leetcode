"""
728. Self Dividing Numbers
Difficulty: Easy
Related Topic: Math

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_divid_list = []
        for num in range(left, right+1):
            if '0' in str(num):
                continue

            if num < 10:
                self_divid_list.append(num)
                continue

            flag = True
            for digit in str(num):
                if not num % int(digit) == 0:
                    flag = False
                    break

            if flag:
                self_divid_list.append(num)

        return self_divid_list

left = 1
right = 22
solution = Solution()
output = solution.selfDividingNumbers(left, right)

print(output)
