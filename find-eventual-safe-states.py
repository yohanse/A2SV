class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse = [[] for i in range(n)]
        incoming = [ 0 for i in range(n)]

        q = deque()
        for i in range(n):
            for j in graph[i]:
                reverse[j].append(i)
            incoming[i] = len(graph[i])
            if not incoming[i]:
                q.append(i)
        ans = []
        while q:
            vertex = q.popleft()
            ans.append(vertex)
            for adjvertex in reverse[vertex]:
                incoming[adjvertex] -= 1
                if not incoming[adjvertex]:
                    q.append(adjvertex)

        return sorted(ans)