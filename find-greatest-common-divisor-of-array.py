class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        a = b = nums[0]
        for i in nums:
            a = min(a, i)
            b = max(b, i)
        
        return gcd(a, b)