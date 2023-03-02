class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0:1}
        total, answer = 0, 0
        for num in nums:
            total += num 
            answer += prefix_sum.get(total - goal, 0)
            prefix_sum[total] = prefix_sum.get(total, 0) + 1
        return answer