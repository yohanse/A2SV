class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}

        for start, end in edges:
            graph[end].append(start)

        res = []
        for i in range(n):
            if not graph[i]:
                res.append(i)
        
        return res