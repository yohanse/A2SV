class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def rec(n):
            if n == 1:
                return 20
            if n == 0:
                return 1
            if n % 2 == 1:
                return ((rec(n//2)**2) * 20) % (10**9 + 7)
            return (rec(n//2)**2) % (10**9 + 7)

        result = rec(n // 2)
        if n % 2:
            result *= 5
        return result % (10**9 + 7)