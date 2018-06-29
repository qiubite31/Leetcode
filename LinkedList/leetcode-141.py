"""
141. Linked List Cycle
Difficulty: Easy
Related Topic: Linked List

141. Linked List Cycle
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while slow and slow.next:
            slow = slow.next
            fast = None if fast is None or fast.next is None else fast.next.next
            if slow == fast:
                return True
        else:
            return False

solution = Solution()
output = solution.hasCycle()