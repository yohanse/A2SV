# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(root):
            if not root:
                return
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        q = [target.val]
        visite = set([target.val])
        for i in range(k):
            t = []
            for i in q:
                for j in graph[i]:
                    if j not in visite:
                        t.append(j)
                        visite.add(j)
            q = t
            if not q:
                break
        return q