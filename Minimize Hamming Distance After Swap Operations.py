class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        graph = [set() for i in range(N)]

        for a, b in allowedSwaps:
            graph[a].add(b)
            graph[b].add(a)

        answer = 0
        visite = set()
        def dfs(vertex):
            stack = [vertex]
            group1, group2 = {source[vertex]: 1}, {target[vertex]: 1}
            visite.add(vertex)
            while stack:
                vertx = stack.pop()
                for adjvertex in graph[vertx]:
                    if adjvertex not in visite:
                        stack.append(adjvertex)
                        visite.add(adjvertex)
                        group1[source[adjvertex]] = group1.get(source[adjvertex], 0) + 1
                        group2[target[adjvertex]] = group2.get(target[adjvertex], 0) + 1

            answer = 0       
            for num in group1:
                answer += min(group2.get(num, 0), group1[num])
            return answer
        
        for i in range(N):
            if i not in visite:
                answer += dfs(i)

        return N - answer