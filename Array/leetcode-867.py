"""
867. Transpose Matrix
Difficulty: Easy
Related Topic: Array

867. Transpose Matrix
"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(row) for row in zip(*A)]

    def transpose2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # import copy
        # A_T = [[0]*len(A[0])]*deepcopy(len(A))
        A_T = []
        # print(A_T)
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row = row + [A[j][i]]

                # print(row)

            A_T.append(row)
            # print(A_T)

        return A_T


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
output = solution.transpose2(A)

print(output)
