class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        top=-1
        length=len(temperatures)
        ans=[0]*length
        for i,value in enumerate(temperatures):
            while top!=-1 and stack[top][0]<value:
                count=stack[top][1]
                ans[count]=i-count
                stack.pop()
                top=top-1
            top=top+1
            stack.append([value,i])
        return ans