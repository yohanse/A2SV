# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def dfs(root,path):
            if not root:return
            if root.left==None and root.right==None:
                temp=path+"->"+str(root.val)
                
                res.append(temp[2:])
                return
            dfs(root.left,path+"->"+str(root.val))
            dfs(root.right,path+"->"+str(root.val))
        dfs(root,"")
        return res