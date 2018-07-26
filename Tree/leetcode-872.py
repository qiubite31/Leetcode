"""
872. Leaf-Similar Trees
Difficulty: Easy
Related Topic: Tree, Recursive

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:

Both of the given trees will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def traversal(leaf, root):
            if root is None:
                return None

            if root.left is None and root.right is None:
                leaf.append(root.val)

            traversal(leaf, root.left)
            traversal(leaf, root.right)

            return leaf

        return traversal([], root1) == traversal([], root2)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

root2 = TreeNode(5)
root2.left = TreeNode(1)
# root2.right = TreeNode(2)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(13)


solution = Solution()
output = solution.leafSimilar(root, root2)

print(output)
