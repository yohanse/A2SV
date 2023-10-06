class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        Graph=defaultdict(list)
        N,ans=len(values),[]
        for i in range(N):
            Graph[equations[i][0]].append((equations[i][1],values[i]))
            Graph[equations[i][1]].append((equations[i][0],1/values[i]))
        for no,dno in queries:
            queue=[(no,1)]
            visite=set([no])
            if no==dno:
                if no not in Graph:ans.append(-1.0000)
                else:ans.append(1.000)
            else:
                while queue:
                    vertex,value=queue.pop(0)
                    if vertex == dno:
                        ans.append(value)
                        break
                    for adjvertex,factor in Graph[vertex]:
                        if adjvertex not in visite:
                            queue.append((adjvertex,factor*value)) 
                            visite.add(adjvertex)
                else:
                    ans.append(-1)
        return ans