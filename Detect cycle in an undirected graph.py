from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        v = len(adj)
        incoming = [0 for i in range(v)]
        for i in range(v):
          incoming[i] = len(adj[i])
          
        count = 0
        q = deque()
        for i in range(v):
            if incoming[i] == 1 or incoming[i] == 0:
                q.append(i)

        while q:
            count += 1
            vertex = q.popleft()
            for adjvertex in adj[vertex]:
                incoming[adjvertex] -= 1
                if incoming[adjvertex] == 1:
                    incoming[adjvertex] = -1
                    q.append(adjvertex)
                          
        if count == v:
            return 0
        return 1