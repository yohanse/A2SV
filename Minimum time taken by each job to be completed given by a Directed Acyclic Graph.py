from typing import List

from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        incoming = [0 for i in range(n)]
        ans = [1 for i in range(n)]
    
        for a, b in edges:
            a, b = a - 1, b - 1
            graph[a].append(b)
            incoming[b] += 1
        
        q = deque()
        for i in range(n):
            if incoming[i] == 0:
                q.append(i)
                
        while q:
            vertex = q.popleft()
            for adjvertex in graph[vertex]:
                incoming[adjvertex] -= 1
                ans[adjvertex] = max(ans[adjvertex], ans[vertex] + 1)
                if incoming[adjvertex] == 0:
                    q.append(adjvertex)
                    
        ans = list(map(str, ans))
        return " ".join(ans)
