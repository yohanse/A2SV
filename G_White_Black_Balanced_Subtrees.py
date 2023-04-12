import sys
input = sys.stdin.readline
def dfs(vertex):
    if not tree[vertex]:
        return 0, change[color[vertex]]
    
    c, ans = 0, 0
    for adjvertex in tree[vertex]:
        num = dfs(adjvertex)
        ans += num[0]
        c += num[1]
    c += change[color[vertex]]
    ans += 1 if c == 0 else 0
    
    return ans, c




t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    color = input()
    tree = [[]for i in range(n)]
    for i in range(n - 1):
        parent = nums[i] - 1
        tree[parent].append(i + 1)
    change = {"W":1, "B":-1}
    curr = [0] * n
    stack = [(0, 0, 0)]
    visite = set()
    while stack:
        parent, vertex, count = stack[-1]
        if not tree[vertex] or vertex in visite:
            curr[vertex] += change[color[vertex]]
            curr[parent] += curr[vertex]
            visite.add(vertex)
            stack.pop()
        else:

            for adjvertex in tree[vertex]:
                stack.append((vertex, adjvertex, count))
            visite.add(vertex)
    print(curr.count(0))