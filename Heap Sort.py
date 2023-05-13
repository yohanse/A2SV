#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        p = (i - 1) // 2
        while i != 0 and arr[(i - 1) // 2] < arr[i]:
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = (i - 1) // 2
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        last = n - 1
        for i in range(n):
            arr[0], arr[last] = arr[last], arr[0]
            self.down(last)
            last -= 1
    
    def down(self, req):
        i = 0
        while i * 2 + 2 < req and arr[i] < max(arr[i * 2 + 2], arr[i * 2 + 1]):
            if arr[i * 2 + 2] > arr[i * 2 + 1]:
                arr[i], arr[i * 2 + 2] = arr[i * 2 + 2], arr[i]
                i = i * 2 + 2
            else:
                arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
                i = i * 2 + 1
        if i * 2 + 1 < req and arr[i] < arr[i * 2 + 1]:
            arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
