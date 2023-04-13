class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        N = right + 1
        prime = [True for i in range(N)]
        prime[0] = prime[1] = False
        res = []
        for i in range(2, N):
            if prime[i]:
                res.append(i)
                j = i * i
                while j < N:
                    prime[j] = False
                    j += i

        ans = [-1, -1]
        index = bisect_left(res, left)
        for i in range(index, len(res)):
            if ans[0] == -1:
                ans[0] = res[i]
            elif ans[1] == -1: 
                ans[1] = res[i]
            else:
                if ans[1] - ans[0] > res[i] - prev:
                    ans = [prev, res[i]]
            prev = res[i]

        if ans[1] == -1:
            return [-1, -1]
        return ans