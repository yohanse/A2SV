# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr, data1, data2 = root, p.val, q.val
        while curr:
            if min(data1, data2) > curr.val:
                curr = curr.right
            elif max(data1, data2) < curr.val:
                curr = curr.left
            else:
                return curr