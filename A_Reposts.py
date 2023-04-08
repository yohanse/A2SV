from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    name1, word, name2 = list(input().split())
    name1, name2 = name1.lower(), name2.lower()
    graph[name2].append(name1)


def dfs(name, res):
    if graph[name] == []:
        return res
    ans = 0
    for name2 in graph[name]:
        ans = max(ans, dfs(name2, res + 1))

    return ans

print(dfs("polycarp", 1))