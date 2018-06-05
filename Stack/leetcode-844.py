"""
844. Backspace String Compare
Difficulty: Easy
Related Topic: Stack

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
 
Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S = []
        stack_T = []
        for s in S:
            if not s == '#':
                stack_S.append(s)
            else:
                if stack_S:
                    stack_S.pop()

        for t in T:
            if not t == '#':
                stack_T.append(t)
            else:
                if stack_T:
                    stack_T.pop()

        if stack_S == stack_T:
            return True
        else:
            return False

S = "ab#c"
T = "ad#c"
solution = Solution()
output = solution.backspaceCompare(S, T)

print(output)
