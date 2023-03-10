# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 0, 0, 0

            left = rec(node.left)
            right = rec(node.right)

            if node.val == ((left[0] + right[0] + node.val)//(left[1] + right[1] + 1)):
                return left[0] + right[0] + node.val, left[1] + right[1] + 1, left[2] + right[2] + 1

            return left[0] + right[0] + node.val, left[1] + right[1] + 1, left[2] + right[2]

        return rec(root)[2]