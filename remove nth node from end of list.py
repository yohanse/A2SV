# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return -1
        length=0
        current=head
        head1=head
        while current!=None:
            current=current.next
            length=length+1
        index=length-n
        length=0
        if index==0:
            head1=head.next
            return head1
        while length<index:
            length=length+1
            per=head
            head=head.next
            if head!=None:
                joo=head.next
            else:
                joo=None
        per.next=joo
        return head