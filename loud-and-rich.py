class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = [[] for i in range(n)]
        answer = [i for i in range(n)]
        incoming = [0 for i in range(n)]

        for a, b in richer:
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

                if  quiet[answer[vertex]] < quiet[answer[adjvertex]]:
                    answer[adjvertex] = answer[vertex]

                if incoming[adjvertex] == 0:
                    q.append(adjvertex)

        return answer