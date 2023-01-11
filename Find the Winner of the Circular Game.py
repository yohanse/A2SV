class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        m = [i for i in range(1,n+1)]
        k -= 1
        b = 0
        while n != 1:
            p = (b + k)%n
            m.pop(p)
            b = p%n
            n -= 1
        return m[0]