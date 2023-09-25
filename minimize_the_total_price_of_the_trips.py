class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        m = len(trips)
        graph = [[] for i in range(n)]

        dp = [0 for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(m):
            start, end = trips[i]
            path = [i for i in range(n)]
            q = deque([start])
            visite = set([start])

            while q:
                vertex = q.popleft()

                if vertex == end:
                    while end != path[end]:
                        dp[end] += 1
                        end = path[end]
                    dp[end] += 1

                for adjvertex in graph[vertex]:
                    if adjvertex not in visite:
                        path[adjvertex] = vertex
                        q.append(adjvertex)
                        visite.add(adjvertex)

        dp = [dp[i] * price[i] for i in range(n)]
        memo = {}
        def dfs(vertex, parent, can_you):
            if len(graph[vertex]) == 1:
                if can_you:
                    return dp[vertex] // 2
                return dp[vertex]

            if (vertex, can_you) in memo:
                return memo[(vertex, can_you)]

            half = halfNot = 0
            for adjvertex in graph[vertex]:
                if parent != adjvertex:
                    half += dfs(adjvertex, vertex, True)
                    halfNot += dfs(adjvertex, vertex, False)
            
            if can_you:
                memo[(vertex, can_you)] = min(halfNot + dp[vertex] // 2, half + dp[vertex])
            else:
                memo[(vertex, can_you)] = dp[vertex] + min(halfNot, half)
            return memo[(vertex, can_you)]
        
        
        for i in range(n):
            if len(graph[i]) > 1:
                return dfs(i, -1, True)
        if n == 2:
            return min(dp[0] + dp[1] // 2, dp[1] + dp[0] // 2)
        return dp[0] // 2       