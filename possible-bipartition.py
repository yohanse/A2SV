class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        Graph={i:[] for i in range(1,n+1)}
        for v1,v2 in dislikes:
            Graph[v2].append(v1)
            Graph[v1].append(v2)
        
        helper=[None for i in range(n)]
        # vertex=0
        # helper[vertex]=False
        # q=deque([vertex+1])
        # while q:
        #     vertex=q.popleft()
        #     group=helper[vertex-1]
        #     for adjvertex in Graph[vertex]:
        #         if helper[adjvertex-1]==None:
        #             q.append(adjvertex)
        #             helper[adjvertex-1] = not group
        #         elif group == helper[adjvertex-1]:
        #             return False
        # return True
        



        for vertex in range(n):
            if helper[vertex]==None:
                helper[vertex]=True
                q=deque([vertex+1])
                while q:
                    vertex=q.popleft()
                    group=helper[vertex-1]
                    for adjvertex in Graph[vertex]:
                        if helper[adjvertex-1]==None:
                            q.append(adjvertex)
                            helper[adjvertex-1] = not group
                        elif group == helper[adjvertex-1]:
                            return False
        return True