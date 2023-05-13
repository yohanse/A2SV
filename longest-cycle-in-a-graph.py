class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        incoming = [0 for i in range(n)]

        for i in edges:
            if i != -1:
                incoming[i] += 1
        
        
        q = deque()
        for i, v in enumerate(incoming):
            if v == 0:
                q.append(i)
        
        while q:
            v = q.popleft()
            v = edges[v]
            if v != -1:
                incoming[v] -= 1
                if incoming[v] == 0:
                    q.append(v)
       
        ans = -1
        for i in range(n):
            count = 0
            while incoming[i] != 0:
                incoming[i] -= 1
                i = edges[i]
                count += 1
                ans = max(ans, count)
        
        return ans