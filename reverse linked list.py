# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        current=None
        while head!=None:
            ans.insert(0,head)
            head=head.next
        if len(ans)==1:
            current=ans[0]
        else:
            for i in range(len(ans)-1):
                ans[i].next=ans[i+1]
                current=ans[0]
                ans[-1].next=None
        return current
            