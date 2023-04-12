class Solution:
    def findComplement(self, num: int) -> int:
        last, temp = 0, num
        while num:
            last = last << 1
            last = last | 1
            num = num >> 1
        return last ^ temp