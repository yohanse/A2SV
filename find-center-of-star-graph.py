class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        N=len(edges)+1
        Graph={i:[] for i in range(1,N+1)}
        for v1,v2 in edges:
            Graph[v1].append(v2)
            Graph[v2].append(v1)
        for vertex in Graph:
            if len(Graph[vertex])==N-1:
                return vertex