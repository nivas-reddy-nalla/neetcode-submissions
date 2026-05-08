# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy

        head1, head2 = list1, list2

        while head1 and head2:
            if head1.val <= head2.val:
                dummy.next = ListNode(head1.val)
                head1 = head1.next
            else:
                dummy.next = ListNode(head2.val)
                head2 = head2.next
            dummy = dummy.next
        
        while head1:
            dummy.next = ListNode(head1.val)
            head1 = head1.next
            dummy = dummy.next
        
        while head2:
            dummy.next = ListNode(head2.val)
            head2 = head2.next
            dummy = dummy.next
        
        return ans.next
        