class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [0 for i in range(n)]
        for vertex1, vertex2 in roads:
            graph[vertex1] += 1
            graph[vertex2] += 1
        
        roads = set(list(map(tuple, roads)))
        res = 0

        for v1 in range(n):
            for v2 in range(v1 + 1, n):
                ans = 0
                if (v1, v2) in roads or (v2, v1) in roads:
                    ans = 1
                res = max(res, graph[v2] + graph[v1] - ans)

        return res