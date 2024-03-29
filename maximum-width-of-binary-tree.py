# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        answer = 1
        while stack:
            temp = []
            for node, index in stack:
                if node.left:
                    temp.append((node.left, index * 2))
                if node.right:
                    temp.append((node.right, index * 2 + 1))
                    
            if temp:
                answer = max(answer, temp[-1][1] - temp[0][1] + 1)
            stack = temp
        return answer