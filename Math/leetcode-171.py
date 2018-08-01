"""
171. Excel Sheet Column Number
Difficulty: Easy
Related Topic: Math, Digital root

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        import string

        char_dict = dict(zip(string.ascii_uppercase, [i for i in range(1, 27, 1)]))
        # print(char_dict)

        digit_len = len(s)
        col_num = 0
        for idx, char in enumerate(s):
            digit = char_dict[char]
            col_num += digit * math.pow(26, digit_len-idx-1)

        return int(col_num)


s = 'ABC'
solution = Solution()
output = solution.titleToNumber(s)

print(output)
