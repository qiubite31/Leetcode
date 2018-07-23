"""
709. To Lower Case
Difficulty: Easy
Related Topic: String

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        import string
        letter_mapping = dict(zip(string.ascii_lowercase + string.ascii_uppercase, string.ascii_lowercase*2))

        str_lower = ''
        for char in str:
            try:
                str_lower = str_lower + letter_mapping[char]
            except:
                str_lower = str_lower + char

        return str_lower




S = "LOVELY"
solution = Solution()
output = solution.toLowerCase(S)

print(output)
