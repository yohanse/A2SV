class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:return strs[0]
        ans=''
        final=False
        for i in range(len(strs[0])):
            check=False
            for j in range(1,len(strs)):
                check=True
                if i==len(strs[j]):return ans
                if strs[j-1][i]!=strs[j][i]:
                    final=True
                    break

            else:
                if check:ans+=strs[j-1][i]
            if final:break
        return ans