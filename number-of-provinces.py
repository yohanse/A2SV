class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows,cols=len(isConnected),len(isConnected[0])
        Graph={i:[] for i in range(rows)}
        for r in range(rows):
            for c in range(r+1,cols):
                if isConnected[r][c]==1:
                    Graph[r].append(c)
                    Graph[c].append(r)
        visited=set()
        def bfs(vertex):
            stack=[vertex]
            while stack:
                vertex=stack.pop()
                for adjvertex in Graph[vertex]:
                    if adjvertex not in visited:
                        visited.add(adjvertex)
                        stack.append(adjvertex)
        ans=0
        for vertex in Graph:
            if vertex not in visited:
                ans+=1
                bfs(vertex)
        return ans