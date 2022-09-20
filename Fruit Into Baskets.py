class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        slow,fast,ans=0,0,0
        fruit1,fruit2=None,None
        length=len(fruits)
        while fast<length:
            if fruit1==None or fruit1==fruits[fast]:
                fruit1=fruits[fast]
            elif fruit2==None or fruit2==fruits[fast]:
                fruit2=fruits[fast]
            else:
                fruit2=fruits[fast]
                fruit1=fruits[fast-1]
                slow=fast-1
                while slow>=0 and fruit1==fruits[slow-1]:
                    slow=slow-1
            fast=fast+1
            ans=max(ans,fast-slow)
        return ans