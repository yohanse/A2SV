class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel='aeiou'
        count=0
        for i in range(k):
            if s[i] in vowel:
                count=count+1
        ans=count
        for i in range(len(s)-k):
            if s[i] in vowel:
                count=count-1
            if s[i+k] in vowel:
                count=count+1
            ans=max(ans,count)
        return ans