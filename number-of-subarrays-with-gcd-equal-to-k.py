class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        n, count = len(nums), 0
        for i in range(n):
            ans = nums[i]
            for j in range(i, n):
                ans = gcd(ans, nums[j])
                if ans == k:
                    count += 1
                    
                if ans < k:
                    break
        return count