class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        num = []
        for i in range(1, N):
            
            
            if heights[i - 1] < heights[i]:
                if ladders == 0:
                    if num:
                        x = heappop(num)
                        bricks -= min(x, heights[i] - heights[i - 1])
                        heappush(num, max(x, heights[i] - heights[i - 1]))
                    else:
                        bricks -= heights[i] - heights[i - 1]

                else:
                    ladders -= 1
                    heappush(num, heights[i] - heights[i - 1])
            

            if bricks < 0:
                return i - 1
        return N - 1