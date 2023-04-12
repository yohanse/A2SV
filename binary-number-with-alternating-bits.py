class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alternate, temp = 0, n
        while temp:
            check = 1
            if alternate & 1:
                check = 0 

            alternate <<= 1
            alternate |= check
            temp >>= 1
        return alternate == n or ~alternate == n