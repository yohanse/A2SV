class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        temp=[sys.maxsize]*n
        temp[src]=0
        
        
        for i in range(k+1):
            Prices=temp.copy()
            for From,To,Price in flights:
                Prices[To]=min(Prices[To],temp[From]+Price)
            temp=Prices
        return temp[dst] if temp[dst]!=sys.maxsize else -1