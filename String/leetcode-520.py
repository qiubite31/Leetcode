"""
520. Detect Capital
Difficulty: Easy
Related Topic: String

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True

        is_first_capital = False
        upper_cnt = 0
        lower_cnt = 0
        for idx, char in enumerate(word):
            if char.isupper():
                if idx == 0:
                    is_first_capital = char.isupper()
                
                upper_cnt += 1
            else:
                lower_cnt += 1

        if len(word) == upper_cnt:
            return True
        elif len(word) == lower_cnt:
            return True
        else:
            if upper_cnt == 1 and is_first_capital:
                return True
            else:
                return False

word = "FlaG"
solution = Solution()
output = solution.detectCapitalUse(word)

print(output)
