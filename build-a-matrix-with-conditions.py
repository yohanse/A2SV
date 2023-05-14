class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def toplogical(edges):
            edges = list(set([(a, b) for a, b in edges]))
            incoming = [0 for i in range(k)]
            graph = [[] for i in range(k)]
            answer = [0 for i in range(k)]
            for a, b in edges:
                a, b = a - 1, b - 1
                incoming[b] += 1
                graph[a].append(b)

            index = 0
            for i in range(k):
                if not incoming[i]:
                    q = deque([i])
                    while q:
                        vertex = q.popleft()
                        answer[vertex] = index
                        index += 1
                        for adjvertex in graph[vertex]:
                            incoming[adjvertex] -= 1
                            if not incoming[adjvertex]:
                                incoming[adjvertex] -= 1
                                q.append(adjvertex)
            if index != k:
                return []
            return answer
        
        row = toplogical(rowConditions)
        col = toplogical(colConditions)
        if row == [] or col == []:
            return []

        matrix = [[0 for i in range(k)] for i in range(k)]
        for i in range(k):
            matrix[row[i]][col[i]] = i + 1
        return matrix