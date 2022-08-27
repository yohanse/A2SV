# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        ans=head
        ans1=head
        head=head.next
        while head!=None:
            if ans1.val==head.val:
                if head.next==None:
                    ans1.next=None
                head=head.next
            else:
                ans1.next=head
                head=head.next
                ans1=ans1.next
        return ans