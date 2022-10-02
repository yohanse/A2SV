class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index=[]
        length1=len(nums1)
        length=len(nums2)
        ans=[-1]*length
        stack=[]
        top=-1
        for i in range(length):
            while top!=-1 and stack[top]<nums2[i]:
                ans[index.pop()]=nums2[i]
                stack.pop()
                top=top-1
            top=top+1
            stack.append(nums2[i])
            index.append(i)
        stack=[]
        for i in range(length1):
            for j in range(length):
                if nums1[i]==nums2[j]:
                    stack.append(ans[j])
                    break
        return stack