class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        arr = [set([i]) for i in range(numCourses)]
        visite = set()
        def dfs(vertex):
            if vertex in visite:
                return

            visite.add(vertex)
            for adjvertex in graph[vertex]:
                dfs(adjvertex)
                for i in arr[adjvertex]:
                    arr[vertex].add(i)

        for i in range(numCourses):
            if i not in visite:
                dfs(i)
        
        ans = []
        for a, b in queries:
            ans.append(b in arr[a])
        return ans