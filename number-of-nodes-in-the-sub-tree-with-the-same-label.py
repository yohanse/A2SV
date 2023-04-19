class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for i in range(n)]
        answer = [0 for i in range(n)]

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        visite = set()
        def dfs(vertex):
            visite.add(vertex)
            letter = [0 for i in range(26)]
            for adjvertex in graph[vertex]:
                if adjvertex not in visite:
                    left = dfs(adjvertex)
                    for i in range(26):
                        letter[i] += left[i]
            
            l = labels[vertex]
            letter[ord(l) - ord("a")] += 1
            answer[vertex] = letter[ord(l) - ord("a")]
            return letter

        dfs(0)
        return answer