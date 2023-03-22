# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]
        dic = {0:1}
        def rec(root, tot):
            if not root:
                return
            
            need = tot + root.val - targetSum
            ans[0] += dic.get(need, 0)
            dic[tot + root.val] = dic.get(tot + root.val, 0) + 1
            rec(root.left, tot + root.val)
            rec(root.right, tot + root.val)
            dic[tot + root.val] -= 1

        rec(root, 0)
        return ans[0]