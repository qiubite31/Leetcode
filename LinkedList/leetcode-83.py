"""
83. Remove Duplicates from Sorted List
Difficulty: Easy
Related Topic: Linked List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        # head = curr_node
        while curr_node is not None:    
            if prev_node and curr_node:
                if prev_node.val == curr_node.val:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    
            else:
                prev_node = curr_node
                curr_node = curr_node.next
            
            
        return head

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(3)

solution = Solution()
output = solution.deleteDuplicates(l1)

print(output)