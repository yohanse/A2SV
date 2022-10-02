class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        stack=[]
        top=-1
        index={n:i for i,n in enumerate(nums1)}
        for i in range(len(nums2)):
            while top!=-1 and stack[top]<nums2[i]:
                val=stack.pop()
                number=index[val]
                ans[number]=nums2[i]
                top=top-1
            if nums2[i] in nums1:
                top=top+1
                stack.append(nums2[i])
        return ans