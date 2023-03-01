class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l1, l2 = {}, {}

        # to creat t with the need
        need = 0
        for i in t:
            l1[i] = l1.get(i, 0) + 1
            if l1[i] == 1:
                need += 1

        have, slow, ans = 0, 0, [0, sys.maxsize]
        for i, l in enumerate(s):

            l2[l] = l2.get(l, 0) + 1
            if l2[l] == l1.get(l, 0):
                have += 1
                
            while have == need:
                l = s[slow]
                if ans[1] - ans[0] + 1 > i - slow + 1:
                    ans = [slow, i]
                    
                if l2[l] == l1.get(l, 0):
                    have -= 1
                l2[l] -= 1
                slow += 1
        return s[ans[0]: ans[1] + 1] if ans[1] != sys.maxsize else ""