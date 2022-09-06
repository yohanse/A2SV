# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        top=-1
        count=[]
        head1=head
        while head!=None:
            if stack==[]:
                stack.append(head)
                top=top+1
            else:
                if stack[top].val<head.val:
                    stack[top].val=head.val
                    top=top-1
                    stack.pop()
                    
                    while top>-1 and stack[top].val<head.val:
                        stack[top].val=head.val
                        top=top-1
                        stack.pop()
                    else:
                        stack.append(head)
                        top=top+1
                else:
                    stack.append(head)
                    top=top+1
            head=head.next
        while top!=-1:
            stack[top].val=0
            top=top-1
        while head1!=None:
            count.append(head1.val)
            head1=head1.next
        return count
            