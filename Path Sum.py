# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ans=[False]
        def dfs(root,tot=0):
            if root.left==None and root.right==None:
                if tot+root.val==targetSum:
                    ans[0]=True
                return
            if root.right:
                dfs(root.right,tot+root.val)
            if root.left:
                dfs(root.left,tot+root.val)
        dfs(root)
        return ans[0]
            