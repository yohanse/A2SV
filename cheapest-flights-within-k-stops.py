class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        Graph={i:[] for i in range(n)}
        for From,To,Price in flights:Graph[From].append((To,Price))
        visite=set()
        @cache
        def dfs(vertex,NumberCitys):
            if vertex==dst:return 0
            elif NumberCitys==k+2 or vertex in visite:return sys.maxsize
            num=sys.maxsize
            for adjvertex,price in Graph[vertex]:
                num=min(num,dfs(adjvertex,NumberCitys+1)+price)
            return num
        res=dfs(src,1)
        return res if res!=sys.maxsize else -1