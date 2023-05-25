class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = sum(nums)
        N = leng = len(nums)
        x = sum(nums)

        for i in range(N - 1, 0, -1):
            avg = x // leng + 1
            if x % leng == 0:
                avg -= 1

            
            if nums[i] > avg:
                nums[i - 1] += nums[i] - avg
                nums[i] = avg

            x -= nums[i]
            leng -= 1

        return max(nums)