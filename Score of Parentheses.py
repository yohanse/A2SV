class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack,r,N=[],0,len(s)
        while r<N:
            if s[r]=="(":
                stack.append("(")
                r+=1
            else:
                tot=0
                while r<N and s[r]!="(":
                    if stack[-1]=="(":
                        if tot!=0:
                            tot=2*tot
                        else:
                            tot=1
                        r+=1
                    else:
                        tot+=stack[-1]
                    stack.pop()
                stack.append(tot)
        return sum(stack)