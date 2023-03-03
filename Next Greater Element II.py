class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length=len(nums)
        stack=[nums[0]]
        index=[0]
        ans=[None]*length
        top=0
        for i in range(1,length):
            while top!=-1 and stack[top]<nums[i]:
                ans[index.pop()]=nums[i]
                top=top-1
                stack.pop()
            top=top+1
            stack.append(nums[i])
            index.append(i)
        k=len(index)
        for i in range(length):
            if k==1:
                break
            while top!=-1 and stack[top]<nums[i]:
                ans[index.pop()]=nums[i]
                top=top-1
                stack.pop()
                k=k-1
        while index!=[]:
            ans[index.pop()]=-1
        return ans