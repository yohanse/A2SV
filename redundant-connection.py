class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N=len(edges)
        parent={i:i for i in range(1,N+1)}
        rank={i:0 for i in range(1,N+1)}
        def find(v):
            if parent[v]==v:return v
            return find(parent[v])
        def union(v1,v2):
            p1,p2=find(v1),find(v2)
            if rank[p1]>rank[p2]:
                parent[p2]=p1
            elif rank[p1]<rank[p2] :
                parent[p1]=p2
            else:
                parent[p2]=p1
                rank[p1]+=1
        for v1,v2 in edges:
            if find(v1)!=find(v2):
                union(v1,v2)
            else:
                r1,r2=v1,v2
        return r1,r2