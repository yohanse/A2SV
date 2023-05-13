class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        N = len(recipes)

        graph = {i:[] for i in recipes}
        incoming = {i:0 for i in recipes}
        supplies = set(supplies)
        q = deque()

        for i in range(N):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in graph:
                    graph[ingredients[i][j]].append(recipes[i])
                    incoming[recipes[i]] += 1
                
                elif ingredients[i][j] not in supplies:
                    incoming[recipes[i]] += 1

            if incoming[recipes[i]] == 0:
                q.append(recipes[i])
        
        ans = []
        while q:
            v = q.popleft()
            ans.append(v)
            for a in graph[v]:
                incoming[a] -= 1
                if incoming[a] == 0:
                    q.append(a)
        return ans