class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)
        graph = defaultdict(list)

        for i in range(n):
            for j in routes[i]:
                graph[j].append(i)
        
        q = deque([(source, 0)])
        visite = set([source])
        mean = set()
        while q:
            vertex, count = q.popleft()

            if vertex == target:
                return count
            
            for i in graph[vertex]:
                if i not in mean:
                    mean.add(i)
                    for adjvertex in routes[i]:
                        if adjvertex not in visite:
                            q.append((adjvertex, count + 1))
                            visite.add(adjvertex)
        return -1