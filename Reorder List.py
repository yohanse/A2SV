# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        root=head
        ans=None
        while fast!=None and fast.next!=None:
            temp=slow
            slow=slow.next
            fast=fast.next
            fast=fast.next
        if fast:
            temp=slow
            slow=slow.next
        temp.next=None
        while slow!=None:
            temp=slow.next
            slow.next=ans
            ans=slow
            slow=temp
        while ans:
            temp=root.next
            temp1=ans.next
            root.next=ans
            ans.next=temp
            ans=temp1
            root=temp