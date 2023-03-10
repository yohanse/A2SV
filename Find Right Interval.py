class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        index = {intervals[i][0]: i for i in range(N)}
        intervals.sort()
        res = [0] * N
        l, r = 0, N
        for start, end in intervals:
            n = self.helper(l, r, end, intervals)
            if n == -1:
                res[index[start]] = -1
            else:
                res[index[start]] = index[intervals[n][0]]

        return res
    
    def helper(self, l, r, target, num):
        while l < r:
            mid = (l + r) // 2
            if num[mid][0]  >= target:
                r = mid
            else:
                l = mid + 1
        if l == len(num):
            return -1
        return l 
