class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        N = len(bombs)
        graph = [[] for i in range(N)]

        for i in range(N):
            for j in range(i + 1, N):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dst = ((x2 - x1)**2 + (y2 - y1)**2)

                if dst <= r1 ** 2:
                    graph[i].append(j)
                
                if dst <= r2 ** 2:
                    graph[j].append(i)

        
        def dfs(vertex):
            num = 1
            for adjvertex in graph[vertex]:
                if adjvertex not in visite:
                    visite.add(adjvertex)
                    num += dfs(adjvertex)
            return num

        ans = 0
        for vertex in range(N):
            visite = set()
            visite.add(vertex)
            ans = max(ans, dfs(vertex))
            
        return ans