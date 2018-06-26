"""
852. Peak Index in a Mountain Array
Difficulty: Easy
Related Topic: Array, Binary Search

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
    def peakIndexInMountainArray2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import math
        l = 0
        r = len(A)-1

        while True:
            mid = l + math.floor((r-l)/2)
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid

            if A[mid] < A[mid+1]:
                l = mid
            else:
                r = mid


A = [0,2,1,0]
solution = Solution()
output = solution.peakIndexInMountainArray2(A)

print(output)
