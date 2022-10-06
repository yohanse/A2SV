class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tot=sum(arr[:k])
        ans=0
        leng=len(arr)
        if tot/k>=threshold:
            ans=1
        for i in range(leng-k):
            tot=tot-arr[i]+arr[i+k]
            if tot/k>=threshold:
                ans=ans+1
        return ans