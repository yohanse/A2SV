class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        dp = [0 for i in range(1001)]

        for i in nums:
            d = 2
            while d * d <= i:
                while i % d == 0:
                    dp[d] = 1
                    i //= d
                d += 1

            if i > 1:
                dp[i] = 1

        return sum(dp)