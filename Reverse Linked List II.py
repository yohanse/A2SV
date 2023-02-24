# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        dummy = ListNode()
        ans = dummy
        check = True
        final = None
        while head and index <= right:
            if left <= index:
                hold = ListNode(head.val)
                if check:
                    final = hold 
                    check = False  
                temp = dummy.next
                dummy.next = hold
                hold.next = temp
            else:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            index += 1
            head = head.next
        if final:
            final.next = head
        return ans.next

