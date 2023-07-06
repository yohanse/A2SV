# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def dynamic(root,flag):
            if not root:return 0
            elif (flag,root) in dp:return dp[(flag,root)]
            elif flag:
                dp[(flag,root)]=dynamic(root.right,False)+dynamic(root.left,False)
                return dp[(flag,root)]
            dp[(flag,root)]=max(dynamic(root.right,True)+dynamic(root.left,True)+root.val,dynamic(root.right,False)+dynamic(root.left,False))
            return dp[(flag,root)]
        return max(dynamic(root,True),dynamic(root,False))