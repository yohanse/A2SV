n = int(input())
graph = [[] for i in range(26)]
author = []
for i in range(n):
    author.append(input().split())


def string(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            graph[ord(a[i]) - ord("a")].append(b[i])

            return
        
for i in range(n - 1):
    string(author[i], author[i + 1])
print(graph)
        
        
        
        
            


