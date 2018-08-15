"""
236. Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Related Topic: Tree, Recursive, LCA

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def traversal(node, tgt):
            if node is None:
                return False

            if node.val == tgt.val:
                return True

            check_exist = traversal(node.left, tgt) or traversal(node.right, tgt)

            return check_exist

        queue = []
        node_order = []
        p_flag = False
        q_flag = False

        queue.append(root)
        while queue:
            node = queue.pop(0)
            node_order.append(node)

            p_flag = True if node == p and not p_flag else p_flag
            q_flag = True if node == q and not q_flag else q_flag

            if p_flag and q_flag:
                p_flag = False
                q_flag = False
                break

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        for node in node_order[::-1]:
            if node == p and not p_flag:
                p_flag = True
            if node == q and not q_flag:
                q_flag = True

            if p_flag and q_flag:
                check_descendants = traversal(node, p) and traversal(node, q)

                if check_descendants:
                    return node

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left.left
q = root.right

solution = Solution()
output = solution.lowestCommonAncestor(root, p, q)

print(output)
