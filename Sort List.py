# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        def split(l):
            if l.next==None:
                return l
            slow,fast=l,l
            while fast!=None and fast.next!=None:
                temp=slow
                slow=slow.next
                fast=fast.next
                fast=fast.next
            temp.next=None
            left=split(slow)
            right=split(l)
            return combo(left,right)
        def combo(temp1,temp2):
            ans=None
            store=None
            while temp1!=None and temp2!=None:
                if temp1.val>temp2.val:
                    if ans==None:
                        ans=temp2
                        store=ans
                    else:
                        ans.next=temp2
                        ans=temp2
                    temp2=temp2.next
                else:
                    if ans==None:
                        ans=temp1
                        store=ans
                    else:
                        ans.next=temp1
                        ans=temp1
                    temp1=temp1.next
            if temp1!=None:
                ans.next=temp1
            if temp2!=None:
                ans.next=temp2
            return store
        return split(head)   