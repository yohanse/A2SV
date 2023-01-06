class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0]*N
        pos, neg = 0, 1
        for i in nums:
            if i > 0:
                res[pos] = i
                pos += 2
            else:
                res[neg] = i 
                neg += 2
        return res