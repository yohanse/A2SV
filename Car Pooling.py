class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans=[trips[0]]
        number=0
        for i in trips:
            number=max(number,i[2])
        count=[0]*(number+1)
        for k in trips:
            num=k[1]
            add=k[0]
            while num<=k[2]-1:
                count[num]=count[num]+add
                num=num+1
        for i in count:
            if i>capacity:
                return False
        return True