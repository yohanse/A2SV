class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        incoming = [0 for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            incoming[a] += 1
            incoming[b] += 1
    
        q = []
        visite = set()
        for i in range(n):
            if incoming[i] == 1 or incoming[i] == 0:
                q.append(i)
                visite.add(i)
        
        while q:
            temp = []
            for i in q:
                for j in graph[i]:
                    if j not in visite:
                        incoming[j] -= 1
                        if incoming[j] == 1:
                            temp.append(j)
                            visite.add(j)
            if temp == []:
                return q
            q = temp