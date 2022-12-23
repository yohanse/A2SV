class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        length_nums=len(nums)
        total_expected=(length_nums*(length_nums+1))//2
        return total_expected-total