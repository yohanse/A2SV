class Solution: 
    def select(self, arr, i):
        mini=arr[i]
        count=i
        for j in range(i,len(arr)):
            if mini>arr[j]:
                mini=arr[j]
                count=j
        return count
    
    def selectionSort(self, arr,n):
        for i in range(n):
            mini=self.select(arr,i)
            arr[mini],arr[i]=arr[i],arr[mini]