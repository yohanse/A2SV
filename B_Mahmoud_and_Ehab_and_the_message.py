n, k, m = list(map(int, input().split()))

words = input().split()
index = {}
for i in range(n):
    index[words[i]] = i

cost = list(map(int, input().split()))
parent = [i for i in range(n)]
min_cost = [i for i in cost]
for i in range(k):
    groups = list(map(int, input().split()))
    rep = groups[1] - 1
    for mem in groups[1:]:
        parent[mem - 1] = rep
        min_cost[rep] = min(min_cost[rep], cost[mem - 1])

final = 0
ans = input().split()
for i in ans:
    final += min_cost[parent[index[i]]]
print(final)
