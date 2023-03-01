# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def rec(l1, l2):
            if not l1 or not l2:
                if l2:
                    return l2
                return l1

            dummy = ListNode()
            if l1.val < l2.val:
                dummy.val = l1.val
                a = rec(l1.next, l2)
                
            else:
                dummy.val = l2.val
                a = rec(l1, l2.next)

            dummy.next = a    
            return dummy    
                
        result = rec(list1, list2)
        return result