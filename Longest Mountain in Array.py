class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        peak=[]
        length=len(arr)
        for i in range(1,length-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                peak.append(i)
        length1=len(peak)
        mountain=0
        for i in range(length1):
            init=peak[i]
            end=peak[i]
            while init>=1 and end<length-1 and arr[init-1]<arr[init] and arr[end]>arr[end+1]:
                init=init-1
                end=end+1
            while init>=1 and arr[init-1]<arr[init]:
                init=init-1
            while end<length-1 and arr[end]>arr[end+1]:
                end=end+1
            mountain=max(mountain,end-init+1)
        return mountain