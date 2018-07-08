"""
506. Relative Ranks
Difficulty: Easy
Related Topic: Hash Table

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        nums_order = sorted(nums, reverse=True)
        rank = dict()
        for idx, num in enumerate(nums_order):
            if idx == 0:
                rank[num] = "Gold Medal"
            elif idx == 1:
                rank[num] = "Silver Medal"
            elif idx == 2:
                rank[num] = "Bronze Medal"
            else:
                rank[num] = str(idx+1)
        
        # print(rank)
        output = [rank[num] for num in nums]
        
        return output


nums = [5, 4, 3, 2, 1]
solution = Solution()
output = solution.findRelativeRanks(nums)

print(output)
