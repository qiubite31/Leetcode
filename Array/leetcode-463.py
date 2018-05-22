"""
463. Island Perimeter
Difficulty: Easy
Related Topic: Array

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # land數量 - land相臨數量*2
        # land相臨數量每次只看左邊和下面
        adjacent_cnt = 0
        land_cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print(grid[row][col])
                if grid[row][col] == 1:
                    land_cnt += 1
                    if col-1 >= 0 and grid[row][col-1] == 1:
                        adjacent_cnt += 1
                        # print('left {} {}'.format(row, col))
                    if row < len(grid)-1 and grid[row+1][col] == 1:
                        adjacent_cnt += 1
                        # print('low {} {}'.format(row, col))
        # print(adjacent_cnt)
        return land_cnt*4 - adjacent_cnt*2



grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]


solution = Solution()
output = solution.islandPerimeter(grid)

print(output)
