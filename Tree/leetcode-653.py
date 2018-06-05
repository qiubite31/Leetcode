"""
653. Two Sum IV - Input is a BST
Difficulty: Easy
Related Topic: Tree, Recursive, Two Pointer

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def traversal(root):
            if not root:
                return []
            
            return traversal(root.left) + [root.val] + traversal(root.right)
        
        flatten_nums = traversal(root)
        # print(flatten_nums)
        
        i = 0
        j = len(flatten_nums)-1
        while i < j:
            if flatten_nums[i] + flatten_nums[j] == k:
                return True
            elif flatten_nums[i] + flatten_nums[j] < k:
                i = i + 1
            else:
                j = j - 1
                
        return False


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right.right = TreeNode(7)

target = 9

solution = Solution()
output = solution.findTarget(tree, 9)

print(output)
