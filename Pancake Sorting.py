class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start=start+1
                end=end-1
        length=len(arr)
        ans=[]
        for i in range(length-1,-1,-1):
            maximum=i
            for j in range(i,-1,-1):
                if arr[maximum]<arr[j]:
                    maximum=j
            if i!=maximum:
                flip(maximum)
                flip(i)
                ans.append(maximum+1)
                ans.append(i+1)
        return ans