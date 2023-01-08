class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        l = 0
        for r in range(N):
            if pivot >= nums[r]:
                if l != r:
                    num = nums.pop(r)
                    nums.insert(l,num)
                l += 1

        r = l = 0
        while r < N and nums[r] <= pivot:
            if pivot != nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
        return nums