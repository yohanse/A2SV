class Solution:
    def c(self,num1,num2,op):
        if op=='+':
            return int(num1)+int(num2)
        elif op=='-':
            return int(num1)-int(num2)
        elif op=='*':
            return int(num1)*int(num2)
        else:
            return int(num1)//int(num2)
    def calculate(self, s: str) -> int:
        operator=[]
        top=-1
        operand=[]
        ope={'+':0,'-':0,'*':1,'/':1}
        ans=''
        for i in s:
            if i==' ':
                continue
            elif i in ope:
                operand.append(ans)
                ans=''
                while top>-1 and ope[operator[top]]>=ope[i]:
                    num2=operand.pop()
                    num1=operand.pop()
                    op=operator.pop()
                    value=self.c(num1,num2,op)
                    operand.append(value)
                    top=top-1
                top=top+1
                operator.append(i)
            else:
                ans=ans+i
        operand.append(ans)
        if operator==[]:
            return ''.join(operand)
        while len(operand)!=1:
            num2=operand.pop()
            num1=operand.pop()
            op=operator.pop()
            value=self.c(num1,num2,op)
            operand.append(value)
        return operand[0]
                    
        