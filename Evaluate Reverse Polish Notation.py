class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        top=-1
        operator=['+','-','*','/']
        for i in tokens:
            if i in operator:
                
                if i=='+':
                    total=int(ans[top-1]) + int(ans[top])
                    ans.pop()
                    ans.pop()
                    top=top-1
                    ans.append(str(total))
                    
                elif i=='-':
                    total=int(ans[top-1])-int(ans[top])
                    ans.pop()
                    ans.pop()
                    top=top-1
                    ans.append(str(total))
                    
                elif i=='*':
                    total=int(ans[top-1])*int(ans[top])
                    ans.pop()
                    ans.pop()
                    top=top-1
                    ans.append(str(total))
                    
                else:
                    total=int(ans[top-1])/int(ans[top])
                    total=int(total)
                    ans.pop()
                    ans.pop()
                    top=top-1
                    ans.append(str(total))
                    
            else:
                ans.append(i)
                top=top+1
        return int(ans[0])