class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow=0
        length=len(s)
        ans=0
        fast=0
        while fast<length:
            if s[fast] in s[slow:fast]:
                while s[slow]!=s[fast]:
                    slow=slow+1
                slow=slow+1  
            fast=fast+1
            ans=max(ans,fast-slow)
        return ans