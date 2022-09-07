class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        top=-1
        letter='abcdefghijklmnopqrstuvwxyz['
        for i in s:
            if i==']':
                space=''
                while stack[top]!='[':
                    space=stack[top]+space
                    top=top-1
                    stack.pop()
                top=top-1
                stack.pop()
                num=''
                while not stack[top] in letter:
                    num=stack[top]+num
                    top=top-1
                    stack.pop()
                    if top==-1:
                        break
                    
                space=space*int(num)
                for j in space:
                    top=top+1
                    stack.append(j)
            else:
                stack.append(i)
                top=top+1
        ans=''
        for k in stack:
            ans=ans+k
        return ans