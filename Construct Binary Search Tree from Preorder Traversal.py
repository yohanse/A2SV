# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_tree(l, r):
            if l > r:
                return None

            num, mid = preorder[l], r + 1
            for i in range(l, r + 1):
                if num < preorder[i]:
                    mid = i
                    break

            node = TreeNode(preorder[l])
            node.left = build_tree(l + 1, mid - 1)
            node.right = build_tree(mid, r)
            return node

        return build_tree(0, len(preorder) - 1)