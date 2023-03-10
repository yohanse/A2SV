class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(last , l , r, a):
            if l == r + 1 and  a > 1:
                return True

            num = False
            for idx in range(l , r + 1):
                cur_num = int(s[l:idx+1])
                if last is None:
                    num = num or backtrack(cur_num , idx + 1, r, a + 1)
                elif last - cur_num ==1:
                    num = num or backtrack(cur_num , idx + 1, r, a + 1)
            
            return num
        
        return backtrack(None, 0, len(s) - 1, 0)