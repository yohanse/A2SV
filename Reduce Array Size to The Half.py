class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans=[]
        arr.sort()
        store=arr[0]
        count=0
        leng=0
        for i in arr:
            if i!=store:
                store=i
                ans.append(count)
                count=0
            count=count+1
            leng=leng+1
        ans.append(count)
        ans.sort(reverse=True)
        leng=leng/2
        slow=0
        count=0
        for i in ans:
            slow=slow+1
            count=count+i
            if count>=leng:
                return slow