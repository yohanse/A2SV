# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        size=0
        while head!=None:
            size=size+1
            head=head.next
        count=0
        while count<(size//2):
            count=count+1
            current=current.next
        return current