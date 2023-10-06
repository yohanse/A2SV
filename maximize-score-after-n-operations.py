class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        print
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        pick = []
        for i in range(1, n):
            for j in range(i):
                pick.append((i, j, gcd(nums[i], nums[j])))
        pick.sort(key = lambda x: x[2])

        final = 2 ** n - 1
        @cache
        def dfs(state, ind, multi):
            
            if state == final:
                return 0
            
            if ind == len(pick):
                return -inf
            
            i, j, v = pick[ind]
            do_not_pick = dfs(state, ind + 1, multi)
            if ((state & (1 << i)) )== 0 and ((state & (1 << j)) == 0):
                state |= 1 << i
                state |= 1 << j
                return max(do_not_pick, dfs(state, ind + 1, multi + 1) + v * multi)
            return do_not_pick
        return dfs(0, 0, 1)