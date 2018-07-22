"""
242. Valid Anagram
Difficulty: Easy
Related Topic: Hash Table

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False

        s_cnt = dict()
        t_cnt = dict()
        for s_char in s:
            try:
                s_cnt[s_char] = s_cnt[s_char] + 1
            except:
                s_cnt[s_char] = 0

        for t_char in t:
            try:
                t_cnt[t_char] = t_cnt[t_char] + 1
            except:
                t_cnt[t_char] = 0

        for t_char, cnt in t_cnt.items():
            try:
                if s_cnt[t_char] == cnt:
                    continue
                else:
                    return False
            except:
                return False

        return True

s = "anagram"
t = "nagaram"

solution = Solution()
output = solution.isAnagram(s, t)

print(output)
