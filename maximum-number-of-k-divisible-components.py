class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = [[] for i in range(n)]
        incoming = [-1 for i in range(n)]
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
            incoming[a] += 1
            incoming[b] += 1
        
        queue = deque()
        count = 0
        incoming[0] += 1
        for vertex in range(n):
            if incoming[vertex] == 0:
                queue.append(vertex)
       
        while queue:
            vertex = queue.popleft()
            count += (values[vertex] % k == 0)
            for adjvertex in tree[vertex]:
                values[adjvertex] += values[vertex]
                incoming[adjvertex] -= 1
                if incoming[adjvertex] == 0:
                    queue.append(adjvertex)
        return count