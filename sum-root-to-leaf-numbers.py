# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(root, ans):
            if not root.right and not root.left:
                return ans*10 + root.val

            num = 0
            if root.left:
                num += preorder(root.left, ans*10 + root.val)
            
            if root.right:
                num += preorder(root.right, ans*10 + root.val)
            
            return num

        return preorder(root, 0)