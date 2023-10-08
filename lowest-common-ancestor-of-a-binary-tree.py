# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = p.val, q.val
        def dfs(root):
            if root == None:
                return "b", 9

            left = dfs(root.left)
            right = dfs(root.right)
          
            if left[0] == "a" and right[0] == "a":
                return "c", root
            
            if left[0] == "a" or "a" == right[0]:
                if root.val == p or root.val == q:
                    return "c", root
                return "a", 9
                
            if root.val == p or root.val == q:
                return "a", 9
            
            if left[0] == "c" or right[0] == "c":
                if left[0] == "c":
                    return "c", left[1]
                return "c", right[1]
            return "b", 9

        return dfs(root)[1]