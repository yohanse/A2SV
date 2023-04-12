class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k-=1
        def quick(l,r):
            pivot = partion(l,r)
            if pivot==k:return nums[k]
            elif pivot<k:return quick(pivot+1,r)
            else:return quick(l,pivot)

        def partion(l,r):
            num,index=nums[r-1],l
            for i in range(l,r):
                if num<=nums[i]:
                    nums[index],nums[i]=nums[i],nums[index]
                    index+=1
            return index-1
        return quick(0,len(nums))