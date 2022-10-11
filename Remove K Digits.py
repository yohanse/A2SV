class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        stack=[]
        top=-1
        for i,value in enumerate(num):
            while k!=0 and top>-1 and stack[top]>value:
                k=k-1
                top=top-1
                stack.pop()
            stack.append(value)
            top=top+1
        stack=stack[:len(stack)-k]
        ans=''
        for value in stack:
            ans=ans+value
        return str(int(ans))