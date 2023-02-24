class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1,N2=len(s1),len(s2)
        l1,l2=[0]*26,[0]*26
        if N2<N1:
            return False
        for i in range(N1):
            l1[ord(s1[i])-ord('a')]+=1
            l2[ord(s2[i])-ord('a')]+=1
        if l1==l2:
            return True
        for i in range(N2-N1):
            l2[ord(s2[i])-ord('a')]-=1
            l2[ord(s2[i+N1])-ord('a')]+=1
            if l1==l2:
                return True
        return False