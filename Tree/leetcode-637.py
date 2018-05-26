"""
637. Average of Levels in Binary Tree
Difficulty: Easy
Related Topic: Tree, Recursive

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # node_list = []
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = 0
        level_dict = {}
        val_list = []
        node_queue = []
        node_queue.append((level, root, ))

        while node_queue:
            cur_level, node = node_queue.pop(0)

            # val_list.append(node.val)
            level_dict.setdefault(cur_level, []).append(node.val)
            # print(node.val)
            
            left_node = node.left
            right_node = node.right
            if left_node:
                node_queue.append((cur_level+1, left_node, ))
            if right_node:
                node_queue.append((cur_level+1, right_node,))

        # print(val_list)
        # print(level_dict)
        avg_level_dict = {key: sum(val)/float(len(val)) for key, val in level_dict.items()}
        print(avg_level_dict)
        return [val for level, val in list(avg_level_dict.items())]

tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
# tree1.left.left = TreeNode(5)
tree1.left.left = TreeNode(15)
tree1.left.right = TreeNode(7)

solution = Solution()
output = solution.averageOfLevels(tree1)

print(output)