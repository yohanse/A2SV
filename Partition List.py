# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great, less = ListNode(), ListNode()
        b1, b2 = great, less

        while head:
            new = ListNode(head.val)

            if head.val < x:
                less.next = new
                less = less.next
                
            else:
                great.next = new
                great = great.next
                
            head = head.next

        less.next = b1.next
        return b2.next      