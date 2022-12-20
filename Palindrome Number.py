class Solution:
    def isPalindrome(self, x: int) -> bool:
        tot=0
        if x<0:return False
        num=x
        while x!=0:
            tot=tot*10 + x%10
            x//=10
        return True if num==tot else False