class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, int(c**0.5)
        while start <= end:
            square = start**2 + end**2
            if square > c:
                end -= 1
            elif square < c:
                start += 1
            else:
                return True
        return False