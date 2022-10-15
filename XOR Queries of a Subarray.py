class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        tot=arr[0]
        ans=[None]*len(queries)
        for i in range(1,len(arr)):
            tot=tot^arr[i]
            arr[i]=tot
        for i,value in enumerate(queries):
            start,end=value[0],value[1]
            if start==0:
                ans[i]=arr[end]
            else:
                ans[i]=arr[start-1]^arr[end]
        return ans