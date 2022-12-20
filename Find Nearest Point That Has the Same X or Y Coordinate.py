class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans=sys.maxsize
        res=None
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                if abs(points[i][0]-x)+abs(points[i][1]-y)<ans:
                    ans=abs(points[i][0]-x)+abs(points[i][1]-y)
                    res=i
        return res if res != None else -1