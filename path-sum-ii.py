# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        def dfs(root,tot=0,value=[]):
            if root.left==None and root.right==None:
                if tot+root.val==targetSum:
                    ans.append(value+[root.val])
                return 
            if root.right:
                dfs(root.right,tot+root.val,value+[root.val])
            if root.left:
                dfs(root.left,tot+root.val,value+[root.val])
        dfs(root)
        return ans