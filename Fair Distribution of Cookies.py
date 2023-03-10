class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        answer = [sys.maxsize]
        children = [0] * k

        def backtrack(index, children, cookies):
            if index == len(cookies):
                answer[0] = min(answer[0], max(children))
                return 
            
            for i in range(k):
                children[i] += cookies[index]
                backtrack(index + 1, children, cookies)
                children[i] -= cookies[index]
                
        backtrack(0, children, cookies)
        return answer[0]