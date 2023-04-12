class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        nums = [[nums[i], i] for i in nums]
        self.nums = nums
        self.k = k
        pivot = self.quick_sort(0, len(nums) - 1)
        res = []
        for l, r in self.nums:
            if l >= pivot:
                res.append(r)
        return res
        
    def quick_sort(self, l, r):
        if r < l:
            return
        pivot = self.partion(l, r)
        if self.k == pivot + 1:
            return self.nums[pivot][0]

        elif self.k < pivot + 1:
            return self.quick_sort(l, pivot - 1)
        else:
            return self.quick_sort(pivot + 1, r)

    def partion(self, l, r):
        num, index = self.nums[r][0], l
        for i in range(l, r + 1):
            if num <= self.nums[i][0]:
                self.nums[index], self.nums[i] = self.nums[i], self.nums[index]
                index += 1
        return index - 1