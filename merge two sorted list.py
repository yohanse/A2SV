# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        ini=head
        while list1!=None and list2!=None:
            if list1.val>=list2.val:
                if head==None:
                    head=list2
                    ini=list2
                else:
                    head.next=list2
                    head=head.next
                list2=list2.next
                continue
            if list1.val<list2.val:
                if head==None:
                    head=list1
                    ini=list1
                else:
                    head.next=list1 
                    head=head.next
                list1=list1.next
        if list1==None:
            head.next=list2
        if list2==None:
            head.next=list1
        return ini.next