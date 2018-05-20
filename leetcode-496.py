"""
496. Next Greater Element I
Difficulty: Easy
Related Topic: Hash

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # 用一個dict紀錄nums裡面每個數字的位置
        nums_loc = {num: idx for idx, num in enumerate(nums)}

        output = []
        # 從紀錄的位置掃到最後看是否有符合條件
        for num in findNums:
            num_loc = nums_loc[num]

            grater_val = -1
            for loc in range(num_loc+1, len(nums)):
                if nums[loc] > num:
                    grater_val = nums[loc]
                    break

            output.append(grater_val)

        return output


# findNums = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
findNums = [2, 4]
nums2 = [1, 2, 3, 4]
solution = Solution()
output = solution.nextGreaterElement(findNums, nums2)

print(output)
