class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        base, pointer, N, res = values[0] - 1, 1, len(values), 0
        while pointer < N:
            res = max(res, base + values[pointer])
            pointer += 1
            base = max(base - 1, values[pointer - 1] - 1)
        return res