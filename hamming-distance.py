class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x and y:
            count += (y & 1) != (x & 1)
            y = y >> 1
            x = x >> 1
        return count + x.bit_count() + y.bit_count()