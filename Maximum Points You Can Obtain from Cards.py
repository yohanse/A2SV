class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        len1=len(cardPoints)
        tot=sum(cardPoints)
        window_size=len1-k
        total=sum(cardPoints[:window_size])
        ans=total
        for i in range(len1-window_size):
            total=total+cardPoints[i+window_size]-cardPoints[i]
            ans=min(ans,total)
        return tot-ans