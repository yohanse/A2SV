class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        num=[None]*len(s)
        for i in s:
            number=int(i[-1])-1
            num[number]=i[:-1]
        ans=''
        for i in num:
            ans=ans+i+' '
        return ans[:-1]