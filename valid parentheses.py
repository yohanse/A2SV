class Solution:
    def isValid(self, s: str) -> bool:
        num=[None]*len(s)
        top=-1
        for i in s:
            if i=='(' or i=='[' or i=='{':
                top=top+1
                num[top]=i
            else:
                if top==-1:
                    return False
                else:
                    if (i==')' and num[top]=='(') or (i==']' and num[top]=='[') or (i=='}' and num[top]=='{'):
                        top=top-1
                    else:
                        return False
        if top!=-1:
            return False
        return True