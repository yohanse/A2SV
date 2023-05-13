class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for i in range(n)]
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[b].append(a)

        visite = set()
        def dfs(vertex):
            if vertex in visite:
                return 

            visite.add(vertex)
            for adjvertex in graph[vertex]:
                dfs(adjvertex)
                ans[vertex].add(adjvertex)
                for i in ans[adjvertex]:
                    ans[vertex].add(i)
        
        for i in range(n):
            if i not in visite:
                dfs(i)
        r = []
        for i in range(n):
            x = list(ans[i])
            x = sorted(x)
            r.append(x)

        return r