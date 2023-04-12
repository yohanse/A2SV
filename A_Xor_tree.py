# even change, odd change, level, count[odd, even]
#

# def dfs(vertex, level):
#     even_change = even_count = 0
#     odd_change = odd_count = 0

#     if level % 2 == 0:
#         even_count += 1
#         even_change += 1 if goal[vertex] != have[vertex] else 0

#     else:
#         odd_count += 1
#         odd_change += 1 if goal[vertex] != have[vertex] else 0

#     if not tree[vertex]:
#         return odd_count, odd_change, even_count, even_change
    
    
#     even_change_temp = even_count_temp = 0
#     odd_change_temp = odd_count_temp = 0

#     for adjvertex in tree[vertex]:
#         num = dfs(adjvertex, level + 1)

#         even_count_temp += num[2]
#         even_change_temp += num[3]

#         odd_count_temp += num[0]
#         odd_change_temp += num[1]

#     return odd_count + odd_count_temp, odd_change + odd_change_temp, even_count + even_count_temp, even_change + even_change_temp


n = int(input())
tree =  [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    tree[v - 1].append(u - 1)
have = input().split()
goal = input().split()
print(tree)
print(dfs(0, 0))
