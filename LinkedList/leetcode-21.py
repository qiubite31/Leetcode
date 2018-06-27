"""
21. Merge Two Sorted Lists
Difficulty: Easy
Related Topic: Linked List

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merge_head = ListNode(-1)
        merge_tail = merge_head
        while not l1 is None or not l2 is None:
            if l1 is None and l2 is not None:
                merge_tail.next = l2
                l2 = l2.next
            elif l2 is None and l1 is not None:
                merge_tail.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    merge_tail.next = l1
                    l1 = l1.next
                else:
                    merge_tail.next = l2
                    l2 = l2.next
                    
            merge_tail = merge_tail.next
           
        return merge_head.next   

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


solution = Solution()
output = solution.mergeTwoLists(l1, l2)

print(output)