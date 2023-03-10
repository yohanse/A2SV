# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = [[] for i in range(2002)]

        level = [(root, 0, 0)]
        while level:
            temp = []
            for node, y, x in level:
                if node.left:
                    temp.append((node.left, y - 1, x + 1))
                if node.right:
                    temp.append((node.right, y + 1, x + 1))
                if node:
                    vertical[y + 1000].append((x, node.val))
            level = temp

        res = []
        for i in range(2002):
            if vertical[i]:
                x = sorted(vertical[i])
                temp = [i[1] for i in x]
                res.append(temp)
        return res