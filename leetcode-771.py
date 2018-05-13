"""
771. Jewels and Stones
Difficulty: Easy
Related Topic: Hash 

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {k: 1 for k in J}
        jewel_cnt = 0
        for s in S:
            try:
                if jewels[s] == 1:
                    jewel_cnt = jewel_cnt + 1
            except KeyError as err:
                continue

        return jewel_cnt

J = 'aA'
S = 'aAAbbbb'
solution = Solution()
output = solution.numJewelsInStones(J, S)

print(output)
