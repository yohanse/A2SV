class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[]
        top=-1
        for i in s:
            if i!=')':
                ans.append(i)
                top=top+1
                
            else:
                string=''
                while ans[top]!='(':
                    string=string+ans[top]
                    ans.pop()
                    top=top-1
                ans.pop()
                top=top-1
                for i in string:
                    ans.append(i)
                    top=top+1
        joo=''
        for i in ans:
            joo=joo+i
        return joo
                