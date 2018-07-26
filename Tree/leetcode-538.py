"""
538. Convert BST to Greater Tree
Difficulty: Easy
Related Topic: Tree, Recursive

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(num_sum, root):
            if root is None:
                return num_sum

            num_sum = traverse(num_sum, root.right)
            num_sum = root.val + num_sum
            root.val = num_sum
            num_sum = traverse(num_sum, root.left)

            return num_sum

        traverse(0, root)
        return root

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

solution = Solution()
output = solution.convertBST(root)

print(output)
