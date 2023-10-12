# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def is_valid_bst_helper(node, min_val, max_val):
            # Base case: an empty tree is a BST
            if not node:
                return True

            # Check if the node's value is within the valid range
            if not (min_val < node.val < max_val):
                return False
            
            # For left subtree, node's value becomes max_val.
            # For right subtree, node's value becomes min_val.
            return (is_valid_bst_helper(node.left, min_val, node.val) and
                    is_valid_bst_helper(node.right, node.val, max_val))

        return is_valid_bst_helper(root, float("-inf"), float("inf"))