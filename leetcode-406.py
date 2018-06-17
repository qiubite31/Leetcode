"""
406. Queue Reconstruction by Height
Difficulty: Medium
Related: Greedy

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people)
        reloc = [[] for _ in people]

        for p in people:
            height = p[0]
            front_people = p[1]
            people_count = 0
            for loc in range(0, len(reloc)):
                if people_count >= front_people and len(reloc[loc]) == 0:
                    reloc[loc] = p
                    break

                loc_height = -1 if len(reloc[loc]) == 0 else reloc[loc][0]
                if loc_height == -1 or reloc[loc][0] >= height:
                    people_count += 1
                    continue
        return reloc


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

solution = Solution()
output = solution.reconstructQueue(people)

print(output)
