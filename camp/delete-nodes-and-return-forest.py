# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        ans = []
        def dfs(root):
            if root is None:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if root.val in to_delete:
                if left:
                    ans.append(left)
                if right:
                    ans.append(right)
                return None
            return TreeNode(root.val, left, right)
        check = dfs(root)
        if check:
            ans.append(check)
        return ans

        