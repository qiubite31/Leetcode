"""
557. Reverse Words in a String III
Difficulty: Easy
Related Topic: String

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        inverse_strs = []
        for chars in s.split(' '):
            inverse_strs.append(chars[::-1])

        return ' '.join(inverse_strs)


S = "Let's take LeetCode contest"
solution = Solution()
output = solution.reverseWords(S)

print(output)
