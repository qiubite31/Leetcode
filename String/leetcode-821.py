"""
821. Shortest Distance to a Character
Difficulty: Easy
Related Topic: String

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """ 
        locs = []
        while True:
            start_loc = 0 if not locs else locs[-1]+1
            idx = S.find(C, start_loc)
            if idx == -1:
                break
            locs.append(idx)

        dists = []
        for idx, char in enumerate(S):
            min_dist = min([abs(idx-loc) for loc in locs])
            dists.append(min_dist)

        return dists


S = "loveleetcode"
C = 'e'
solution = Solution()
output = solution.shortestToChar(S, C)

print(output)
