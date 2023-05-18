class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        disjoint = []
        for i in range(n):
            arr = [0]*26
            arr[ord(s[i]) - ord("a")] = 1
            disjoint.append([i, arr])
        rank = [0] * n

        def dfs(vertex):
            while vertex != disjoint[vertex][0]:
                vertex = disjoint[vertex][0]
                
            return vertex

        for a, b in pairs:
            px, py = dfs(a), dfs(b)
            if rank[px] <= rank[py]:
                if px != py:
                    for i in range(26):
                        disjoint[py][1][i] += disjoint[px][1][i]
                
                disjoint[px][0] = py
                rank[py] = max(rank[py], rank[px] + 1)
            else:
                for i in range(26):
                    disjoint[px][1][i] += disjoint[py][1][i]
                
                disjoint[py][0] = px
                rank[px] = max(rank[py] + 1, rank[px])
        ans = ""
        for i in range(n):
            p = dfs(i)
            
            arr = disjoint[p][1]
            for i in range(26):
                if arr[i] != 0:
                    ans += chr(ord("a") + i)
                    arr[i] -= 1
                    break

        return ans