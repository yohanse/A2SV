class Solution:
    def countOrders(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        dp = {}
        def rec(n, m):
            if n == 0 and m == 0:
                return 1
            
            if (n, m) in dp:
                return dp[(n, m)]

            if n == 0:
                dp[(n, m)] = rec(n + 1, m - 1) * m
            elif m == 0:
                dp[(n, m)] = rec(n - 1, m) * n
            else:
                dp[(n, m)] = rec(n - 1, m) * n + rec(n + 1, m - 1) * m
            return dp[(n, m)] % modulo
        return rec(0, n)