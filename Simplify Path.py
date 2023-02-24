class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path+"/"
        temp=''
        for i in path:
            if i=='/':
                if temp=='..' and stack!=[]:
                    stack.pop()
                elif temp!='..' and temp!='' and temp!='.':
                    stack.append(temp)
                temp=''
            else:
                temp+=i
        print(stack)
        ans='/'.join(stack)
        return '/'+ans