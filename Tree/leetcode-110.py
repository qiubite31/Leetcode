"""
110. Balanced Binary Tree
Difficulty: Easy
Related Topic: Tree, Recursive

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        def checkHeight(node):
            if node is None:
                return 0
            else:
                left_height = checkHeight(node.left)
                right_height = checkHeight(node.right)

                return max(left_height, right_height) +1


        left_height = checkHeight(root.left)
        right_height = checkHeight(root.right)

        check_balance = abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        return check_balance

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
output = solution.isBalanced(root)

print(output)
