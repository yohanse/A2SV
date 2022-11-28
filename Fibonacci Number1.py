class Solution:
    def fib(self, n: int) -> int:
        dp={0:0,1:1}
        def fibo(n):
            if n in dp:return dp[n]
            dp[n]=fibo(n-1)+fibo(n-2)
            return dp[n]
        return fibo(n)