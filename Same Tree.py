# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p, q)]

        while stack:
            cur_p, cur_q = stack.pop()

            if cur_p == None and cur_q == None:
                continue
            elif cur_p == None or cur_q == None or cur_p.val != cur_q.val:
                return False
            
            stack.append((cur_p.left, cur_q.left))
            stack.append((cur_p.right, cur_q.right))

        return True