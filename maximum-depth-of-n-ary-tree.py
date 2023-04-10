"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:return 0
        def dfs(root):
            stack,ans=[[1,root]],1
            while stack:
                path,root=stack.pop()
                if root!=None:
                    for children in root.children:
                        stack.append([path+1,children])
                        ans=max(ans,path+1)
            return ans
        return dfs(root)