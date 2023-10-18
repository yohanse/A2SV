# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        reminder = 0
        dummy = ListNode()
        answer = dummy
        while l1 or l2 or reminder:
            num1, num2 = 0, 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            tot = num1 + num2 + reminder
            reminder = tot//10
            tot = tot % 10
            dummy.next = ListNode(tot)
            dummy = dummy.next
        dummy.next = l1
        if l2:
            dummy.next = l2
        return self.reverse(answer.next)
        
    def reverse(self, head):
        dummy = None
        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        return dummy