class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        Graph = {i:[] for i in range(n)}
        
        for i in range(len(edges)):
            vertex1 = edges[i][0] 
            vertex2 = edges[i][1] 
            weight = succProb[i]

            Graph[vertex1].append((vertex2, weight))
            Graph[vertex2].append((vertex1, weight))
        
        maximum_probability = [[-1,start]]
        visite = set()
        res = 0

        while maximum_probability:
            
            probability, vertex  = heapq.heappop(maximum_probability)
            if probability == 0:
                break
            if vertex == end:
                res = max(res,0-probability)
                continue
            if vertex  in visite:
                continue
            visite.add(vertex)

            for adjvertex, weight in Graph[vertex]:
                if adjvertex not in visite:
                    heapq.heappush(maximum_probability, [probability*weight, adjvertex])
                    
                    

        return res