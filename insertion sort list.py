# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=head
        size=0
        while head!=None:
            key=head.val
            current=head1
            count=0
            while count<size:
                if key<current.val:
                    temp=current.val
                    head.val=current.val
                    current.val=key
                    key=temp
                count=count+1
                current=current.next
            size=size+1
            head=head.next
        return head1          