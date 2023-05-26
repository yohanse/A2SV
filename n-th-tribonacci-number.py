class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1
        for i in range(n - 2):
            first, second, third = second, third, first + second + third
        if n == 0:
            return 0
        return third