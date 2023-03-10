# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        mono_stack = []
        last = -sys.maxsize
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if last == root.val:
                    num, mode = mono_stack.pop()
                    while mono_stack and mono_stack[-1][1] < mode + 1:
                        mono_stack.pop()
                    mono_stack.append((num, mode + 1))

                else:
                    mono_stack.append((root.val, 1))
                last = root.val
                root = root.right

        mono_stack.append((0, 0))
        res = []
        for i in range(1, len(mono_stack)):
            res.append(mono_stack[i - 1][0])
            if mono_stack[i - 1][1] != mono_stack[i][1]:
                break
        
        return res