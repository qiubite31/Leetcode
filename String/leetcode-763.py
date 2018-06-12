"""
763. Partition Labels
Difficulty: Medium
Related Topic: String, Two Pointers

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.


"""
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []

        start = 0
        end = len(S)-1
        max_idx = -1
        while start <= len(S)-1:
            idx = len(S) -1 - S[::-1].index(S[start])
            stop = False
            while not stop:
                chars = set(S[start: idx+1])
                idx = max([len(S) -1 - S[::-1].index(_) for _ in chars])

                if max_idx == idx:
                    stop = True
                else:
                    max_idx = idx
            output.append(S[start: max_idx+1])
            start = max_idx+1

        return [len(s) for s in output]

S = "ababcbacadefegdehijhklij"
solution = Solution()
output = solution.partitionLabels(S)

print(output)
