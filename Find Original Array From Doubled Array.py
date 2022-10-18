class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []
        changed.sort()
        ans=[]
        count=Counter(changed)
        for i in changed:
            if i==0:
                if count[i]>=2:
                    count[i]-=2
                    ans.append(i)
            elif count[i]!=0:
                count[i]=count[i]-1
                if count[2*i]>0:
                    ans.append(i)
                    count[2*i]=count[2*i]-1
        if len(ans)==len(changed)/2:
            return ans
        return []