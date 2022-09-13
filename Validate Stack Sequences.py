class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        top=-1
        for i in range(len(pushed)):
            stack.append(pushed[i])
            top=top+1
            if stack[top]==popped[0]:
                stack.pop()
                top=top-1
                popped=popped[1:]
                while top!=-1:
                    if stack[top]==popped[0]:
                        stack.pop()
                        top=top-1
                        popped=popped[1:]
                    else:
                        break
        if stack==[]:
            return True
        return False
            