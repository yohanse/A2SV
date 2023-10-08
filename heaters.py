class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        r,he,ho=0,0,0
        houses.sort()
        heaters.sort()
        while ho<len(houses) and he<len(heaters):
            if heaters[he]<houses[ho]:
                he+=1
            else:
                if he==0:
                    ans=abs(heaters[he]-houses[ho])
                else:
                    ans=abs(heaters[he]-houses[ho])
                    if ans>abs(heaters[he-1]-houses[ho]):
                        ans=abs(heaters[he-1]-houses[ho])
                r=max(r,ans)
                ho+=1
        while ho<len(houses):
            r=max(r,abs(houses[ho]-heaters[-1]))
            ho+=1
        return r