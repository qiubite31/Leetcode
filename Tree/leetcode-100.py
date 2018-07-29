"""
100. Same Tree
Difficulty: Easy
Related Topic: Tree, Recursive

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traversal(node, root):
            if root is None:
                return None

            node.append(root.val)
            traversal(node, root.left)

            if root.left is None and not root.right is None:
                node.append(None)

            traversal(node, root.right)

            return node

        return traversal([], p) == traversal([], q)

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

root = TreeNode(1)
root.left = TreeNode(2)

root2 = TreeNode(1)
root2.right = TreeNode(2)

solution = Solution()
output = solution.isSameTree2(root, root2)

print(output)
