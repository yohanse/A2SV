class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visite = set([0])
        def postorder(vertex):
            count, have = 0, hasApple[vertex]
            for adjvertex in graph[vertex]:
                if adjvertex not in visite:
                    visite.add(adjvertex)
                    num, is_there = postorder(adjvertex)
                    if is_there:
                        count += num + 1
                        have = True
            return count, have

        return 2 * postorder(0)[0]