class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack=''
        ans=[]
        for fast in range(len(s)-1):
            stack=stack+s[fast]
            for i in stack:
                if i in s[fast+1:]:
                    break
            else:
                ans.append(len(stack))
                stack=''
        if s[-1] in stack or stack=='':
            ans.append(len(stack)+1)
        else:
            ans.append(len(stack))
            ans.append(1)
        return ans