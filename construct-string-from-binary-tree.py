# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root.left and not root.right:
                print(root.val)
                return str(root.val)

            ans = str(root.val)
            if root.left:
                ans += "(" + preorder(root.left) + ")"
            else:
                ans += "()"
            
            if root.right:
                ans += "(" + preorder(root.right) + ")"
            
            return ans

        return preorder(root)