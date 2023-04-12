class Solution:
    def minSteps(self, n: int) -> int:
        def recursive(N, index, ans):
            if N == n:
                return ans
            if N > n:
                return sys.maxsize

            if index == 0:
                return recursive(2 * N, N, ans + 2)

            return min(recursive(N + index, index, ans + 1), 
                        recursive(2 * N, N, ans + 2))

        return recursive(1, 0, 0)