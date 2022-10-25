class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter,l,ans=[0]*26,0,0
        for r,char in enumerate(s):
            index=ord(char)-ord('A')
            letter[index]+=1
            freq=max(letter)
            if r-l+1-freq>k:
                index=ord(s[l])-ord('A')
                letter[index]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans