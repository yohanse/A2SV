# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def postorder(root):

            if not root.left and not root.right:
                return max(0, root.val), root.val

            left, left_res = -sys.maxsize, -sys.maxsize
            right, right_res = -sys.maxsize, -sys.maxsize

            if root.left:
                left, left_res = postorder(root.left)
            
            if root.right:
                right, right_res = postorder(root.right)

            return max(0, left + root.val, right + root.val), max(max(0, left) + max(0, right) + root.val, left_res, right_res)
        
        return postorder(root)[1]