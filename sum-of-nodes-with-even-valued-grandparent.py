# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def rec(grand,father,son):
            if not son:return 0
            return rec(father,False if son.val%2 else True,son.right)+rec(father,False if son.val%2 else True,son.left)+(son.val if grand else 0)
        return rec(False,False,root)