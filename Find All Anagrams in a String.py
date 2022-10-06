class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        length1=len(s)
        length2=len(p)
        number=[0]*26
        for i in p:
            index=ord(i)-97
            number[index]=number[index]+1
        rev=list(number)
        slow=0
        fast=0
        while fast<length1:
            if not (s[fast] in p):
                slow=fast+1
                fast=slow
                continue
            if fast-slow==length2-1:
                for i in s[slow:fast+1]:
                    index=ord(i)-97
                    if number[index]==0:
                        break
                    number[index]=number[index]-1
                else:
                    ans.append(slow)
                    while fast<length1-1 and s[slow]==s[fast+1]:
                        ans.append(slow+1)
                        slow=slow+1
                        fast=fast+1
                slow=slow+1
                number=list(rev)
            fast=fast+1
        return ans