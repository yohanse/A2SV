class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        N, ans = len(timePoints), inf

        for i in range(N):
            first, second = timePoints[i], timePoints[i - 1]
            ans = min(ans, ((int(first[:2]) - int(second[:2])) * 60 + int(first[3:]) - int(second[3:])) % 1440)

        return ans
        