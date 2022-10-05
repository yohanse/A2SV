class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        end=len(tokens)-1
        start=0
        score=0
        if end==0:
            if power>=tokens[0]:
                return 1
            return 0
        while start<end and power>=tokens[start]:
            while power>=tokens[start]:
                power=power-tokens[start]
                score=score+1
                start=start+1
            if score>=1 and end-start>=2:
                power=power+tokens[end]
                score=score-1
                end=end-1
            else:
                break
        return score