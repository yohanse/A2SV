class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = arr + [-sys.maxsize]
        stack,ans,N=[],0,len(arr)
        for i in range(N):
            per=i
            while stack!=[] and stack[-1][0]>arr[i]:
                num,per,index=stack.pop()
                ans+=(index-per+1)*(i-index)*num
            stack.append([arr[i],per,i])
       
        mod=10**9+7
        return ans%mod