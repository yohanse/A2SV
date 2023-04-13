class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        graph = [[] for i in range(n)]

        for i in range(1, n):
            graph[parent[i]].append(i)

        def postorder(vertex):
            if graph[vertex] == []:
                return 1, 1
            
            real_ans, ans = 0, 0
            for adjvertex in graph[vertex]:
                candidate_real_ans, candidate_ans = postorder(adjvertex)
                if s[adjvertex] != s[vertex]:
                    real_ans = max(candidate_real_ans + ans + 1, real_ans)
                    ans = max(candidate_real_ans, ans)

                real_ans = max(real_ans, candidate_ans)
            
            return ans + 1, max(1, real_ans)
        return postorder(0)[1]