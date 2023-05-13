# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if  not lists or len(lists)==0:return None
        def combo(temp1,temp2):
            ans=ListNode()
            store=ans
            while temp1!=None and temp2!=None:
                if temp1.val>temp2.val:
                    ans.next=temp2
                    ans=ans.next
                    temp2=temp2.next
                else:
                    ans.next=temp1
                    ans=ans.next
                    temp1=temp1.next
            if temp1!=None:
                ans.next=temp1
            if temp2!=None:
                ans.next=temp2
            return store.next  
        while len(lists)>1:
            temp=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                l3=combo(l1,l2)
                temp.append(l3)
            lists=temp
        return lists[0]