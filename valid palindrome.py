class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(filter(str.isalnum,s))
        s=s.lower()
        l,r=0,len(s)-1
        
        while r>l:
            if s[r]!=s[l]:return False
            l,r=l+1,r-1
        return True 