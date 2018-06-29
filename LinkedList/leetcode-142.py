"""
142. Linked List Cycle II
Difficulty: Easy
Related Topic: Linked List

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while slow and slow.next:
            slow = slow.next
            fast = None if fast is None or fast.next is None else fast.next.next
            if fast is slow:
                break
        else:
            return None

        slow = head
        while fast is not slow:
            slow = slow.next
            fast = fast.next
        else:
            return slow

head = ListNode(3)
head.next = ListNode(2)
ori_head = head.next
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = ori_head

solution = Solution()
output = solution.detectCycle(head)

print(output)