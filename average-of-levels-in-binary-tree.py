# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        res = []
        while q:
            tot, temp = 0, []
            for node in q:
                tot += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(tot / len(q))
            q = temp
        return res