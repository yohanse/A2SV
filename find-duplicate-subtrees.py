# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        ans1 = set()
        seen_serilize = set()

        def dfs(root):
            if root == None:
                return ""
            
            left = dfs(root.left)
            right = dfs(root.right)
            traverse = str(root.val) + "left" + left + "right" + right
            if traverse in seen_serilize and traverse not in ans1:
                ans.append(root)
                ans1.add(traverse)
            seen_serilize.add(traverse)
            return traverse
        dfs(root)
        return ans