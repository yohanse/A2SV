class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char=set()
        def can_not(a,b):
            c=Counter(a)+Counter(b)
            return max(c.values())>1
        def backtrack(i):
            if i==len(arr):
                return len(char)
            res=0
            if not can_not(char,arr[i]):
                for k in arr[i]:
                    char.add(k)
                res=backtrack(i+1)
                for k in arr[i]:
                    char.remove(k)
            return max(res,backtrack(i+1))
        return backtrack(0)