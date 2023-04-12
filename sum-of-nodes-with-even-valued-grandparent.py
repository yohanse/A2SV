# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def add_node(root):
            stack,temp,count,ans=[root],[],0,0
            while stack:
                root=stack.pop()
                if root:
                    temp.append(root.left)
                    temp.append(root.right)
                    if count==2:ans+=root.val
                if stack==[]:
                    stack=temp.copy()
                    temp=[]
                    count+=1
                    if count==3:break
            return ans

        def dfs(root):
            stack,res=[root],0
            while stack:
                root=stack.pop()
                if root:
                    if root.val%2==0:res+=add_node(root)
                    stack.append(root.left)
                    stack.append(root.right)
            return res
        return dfs(root)