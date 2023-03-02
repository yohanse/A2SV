class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        need = {}
        N = len(s)
        n = N//4

        for i in count:
            if count[i] - n > 0:need[i] = count[i] - n
        
        if len(need) == 0:
            return 0
        have = {}
        a, b = len(need), 0
        slow = 0
        answer = sys.maxsize
        for i, l in enumerate(s):
            have[l] = have.get(l, 0) + 1
            if have[l] == need.get(l, 0):
                b += 1
            while a == b:
                l = s[slow]
                answer = min(i - slow + 1, answer)
                if have[l] == need.get(l, 0):
                    b -= 1
                have[l] -= 1
                slow += 1

        return answer