# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:

            node_1, node_2 = stack.pop()
            if node_1 == None and node_2 == None:
                continue

            elif ((node_1 == None and node_2 != None) or 
                    (node_1 != None and node_2 == None) or 
                    (node_1.val != node_2.val)):
                return False

            else:
                stack.append((node_1.left, node_2.right))
                stack.append((node_1.right, node_2.left))
                
        return True