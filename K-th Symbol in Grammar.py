class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n, s = n - 1, 0
        for i in range(n):
            create = 2**(n - i - 1)
            if create < k:
                s = 1 - s
                k -= create
        return s