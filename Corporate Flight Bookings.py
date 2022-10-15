class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n
        for i in bookings:
            start=i[0]-1
            end=i[1]
            add=i[2]
            ans[start]=ans[start]+add
            if end<n:
                ans[end]=ans[end]-add
        tot=0
        for i in range(n):
            tot=tot+ans[i]
            ans[i]=tot
        return ans