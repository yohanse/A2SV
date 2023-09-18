t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    graph = [set() for i in range(m)]
    for i in range(n):
        x = input()
        for j in range(m):
            graph[j].add(x[j])

    string = 'vika'
    count = 0
    for i in range(m):
        if string[count] in graph[i]:
            count += 1
        
        if count == 4:
            print("YES")
            break
        
    else:
        print("NO")