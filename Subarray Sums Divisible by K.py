class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic, total, answer = {0:1}, 0, 0
        for i, num in enumerate(nums):
            total += num
            answer += dic.get(total % k, 0)
            dic[total % k] = 1 + dic.get(total % k, 0)
        return answer