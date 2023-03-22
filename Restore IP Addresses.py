class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, n = [], len(s)
        
        def backTrack(index, ans):
            if n == index:
                if len(ans) == 4:
                    res.append(".".join(ans))
                return
            
            if len(ans) < 4:
                ans.append(s[index])
                backTrack(index + 1, ans)
                ans.pop()

            if ans[-1][0] != '0':
                ans[-1] += s[index]
                if int(ans[-1]) < 256:
                    backTrack(index + 1, ans)
                ans[-1] = ans[-1][:-1]

                    
        backTrack(1, [str(s[0])])
        return res