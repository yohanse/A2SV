t = int(input())
for i in range(t):
    inp = input()

    disjoint = [i for i in range(len(inp))]
    def dfs(curr):
        while curr != disjoint[curr]:
            curr = disjoint[curr]
        return curr
    
    for i in range(len(inp)):
        if inp[i] == "E":
            px, py = dfs(i), dfs((i + 1) % len(inp))
            disjoint[px] = py
    
    for i in range(len(inp)):
        if inp[i] == "N" and dfs(i) == dfs((i + 1) % len(inp)):
            print("NO")
    else:
        print("YES")
            