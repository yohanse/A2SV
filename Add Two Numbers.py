# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        ans1=ans
        reminder=0
        while l1!=None and l2!=None:
            total=l1.val+l2.val+reminder
            reminder=total//10
            if total>=10:
                total=total%10
            new=ListNode(total)
            ans.next=new
            ans=new
            l1=l1.next
            l2=l2.next
        while l1!=None:
            total=l1.val+reminder
            reminder=total//10
            if total>=10:
                total=total%10
            new=ListNode(total)
            ans.next=new
            ans=new
            l1=l1.next
        while l2!=None:
            total=l2.val+reminder
            reminder=total//10
            if total>=10:
                total=total%10
            new=ListNode(total)
            ans.next=new
            ans=new
            l2=l2.next
        if reminder>=1:
            new=ListNode(reminder)
            ans.next=new
        return ans1.next