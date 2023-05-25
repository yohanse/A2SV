class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        n = len(satisfaction)
        for i in range(n):
            x = 0
            for j in range(i, n):
                x += (j - i + 1) * satisfaction[j]
            ans = max(x, ans)
        return ans