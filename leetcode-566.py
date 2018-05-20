"""
566. Reshape the Matrix
Difficulty: Easy
Related Topic: Array

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""

from itertools import chain
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        from itertools import chain
        flatten_nums = list(chain(*nums))

        reshape_matrix = []
        idx = 0
        for row in range(r):
            reshape_row = []
            for col in range(c):
                try:
                    reshape_row.append(flatten_nums[idx])
                    idx += 1
                except IndexError as err:
                    return nums
                
            reshape_matrix.append(reshape_row)

        return reshape_matrix


nums = [[1, 2], [3, 4]]
r = 2
c = 4
solution = Solution()
output = solution.matrixReshape(nums, r, c)

print(output)
