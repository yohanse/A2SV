class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1,l2=[0]*26,[0]*26
        for i in range(len(s)):
            l1[ord(s[i])-97]+=1
            l2[ord(t[i])-97]+=1
        l2[ord(t[-1])-97]+=1

        for i in range(26):
            if l1[i]!=l2[i]:
                return chr(97+i)