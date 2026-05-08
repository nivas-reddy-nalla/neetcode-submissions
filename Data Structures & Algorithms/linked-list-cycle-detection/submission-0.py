# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        hare, tortoise = head.next, head

        while hare and hare.next:
            if hare == tortoise:
                return True
            tortoise = tortoise.next
            hare = hare.next.next
        return False