# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy1 = dummy
        hold = None
        count = 0
        
        while head:
            if count % k == 0:
                fake = head
                while hold:
                    dummy.next = hold
                    hold = hold.next
                    dummy = dummy.next
                hold = ListNode(head.val)
            else:
                node = ListNode(head.val)
                node.next = hold
                hold = node
            head = head.next
            count += 1

        if count % k == 0:
                fake = head
                while hold:
                    dummy.next = hold
                    hold = hold.next
                    dummy = dummy.next
                
        else:
            dummy.next = fake

        return dummy1.next