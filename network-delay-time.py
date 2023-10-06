class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        Graph={i:[] for i in range(n)}
        for initial,final,weight in times:Graph[initial-1].append([final-1,weight])
        number=[sys.maxsize]*n
        number[k-1]=0
        visite=[False]*n
        def select():
            ans=None
            for i in range(n):
                if visite[i]==False and number[i]!=sys.maxsize:
                    if ans==None:ans=[number[i],i]
                    elif ans[0]>number[i]:ans=[number[i],i]
            if ans==None:return False
            visite[ans[1]]=True
            return ans

        def dijsktra():
            for i in range(n):
                sel=select()
                if sel==False:break
                for adjvertex,weight in Graph[sel[1]]:
                    if number[adjvertex]>sel[0]+weight:
                        number[adjvertex]=sel[0]+weight
        dijsktra()
        num=max(number)
        if num==sys.maxsize:return -1
        return num