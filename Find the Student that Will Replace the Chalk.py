class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot=0
        for value in chalk:
            tot=tot+value
        n=k//tot
        k=k-(n*tot)
        for i,value in enumerate(chalk):
            k=k-value
            if k<0:
                return i