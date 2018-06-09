"""
814. Binary Tree Pruning
Difficulty: Medium
Related Topic: Tree, Recursive

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def _pruneNode(root):
            if root is None:
                return 0
            else:
                return root.val + _pruneNode(root.left) + _pruneNode(root.right)

        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if _pruneNode(root):
            return root
        else:
            return None
    def pruneTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        root.left = self.pruneTree2(root.left)
        root.right = self.pruneTree2(root.right)

        if root.val:
            return root
        else:
            return root if root.left or root.right else None
        

# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(1)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)

# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(0)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)
# root.left.left.left = TreeNode(0)

root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
output = solution.pruneTree2(root)

print(output)
