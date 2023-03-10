# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue,res,tmp=[root],[],[]
        have,need,null,l=0,1,0,1
        while queue:
            root=queue.pop(0)
            if root:
                queue.append(root.left)
                queue.append(root.right)
                tmp.append(root.val)
            else:
                null+=1
            have+=1
            if have==need:
                if tmp:
                    res.append(tmp.copy())
                tmp=[]
                need=2**l
                null=null*2
                need=need-null
                l+=1
                have=0
        return res