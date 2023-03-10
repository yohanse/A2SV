# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:return root2
            
        merge_tree = root1
        stack = [(None, root1, None, root2, True)]
        while stack:
            parent_root1, root1, parent_root2, root2, comes_from = stack.pop()
            if not root1:
                if comes_from:
                    parent_root1.left = root2
                else:
                    parent_root1.right = root2

            elif root2:
                root1.val += root2.val
                stack.append((root1, root1.left, root2, root2.left, True))
                stack.append((root1, root1.right, root2, root2.right, False))

        return merge_tree     