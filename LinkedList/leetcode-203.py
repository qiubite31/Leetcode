"""
203. Remove Linked List Elements
Difficulty: Easy
Related Topic: Linked List

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        while curr_node is not None:
            if curr_node.val == val:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    head = curr_node.next
            else:
                prev_node = curr_node
                
            curr_node = curr_node.next
            
        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(6)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)


solution = Solution()
output = solution.removeElements(l, 6)

print(output)
