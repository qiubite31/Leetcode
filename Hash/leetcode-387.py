"""
387. First Unique Character in a String
Difficulty: Easy
Related Topic: Hash Table

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        for char in s:
            char_dict[char] = char_dict.setdefault(char, 0) +1

        min_idx = len(s)
        for char, cnt in char_dict.items():
            if not cnt == 1:
                continue

            idx = s.index(char)
            if idx < min_idx:
                min_idx = idx

        if not min_idx == len(s):
            return min_idx
        else:
            return -1

s = "leetcode"

solution = Solution()
output = solution.firstUniqChar(s)

print(output)
