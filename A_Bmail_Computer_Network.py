n = int(input())

dic = {i:[] for i in range(1, n + 1)}
num = list(map(int, input().split()))
for i in range(2, n + 1):
    sup = num[i - 2]
    dic[i].append(sup)

stack = [n]
target = 1
res = [n]
while stack:
    root = stack.pop()
    for node in dic[root]:
        res.append(node)
        stack.append(node)

    if root == 1:
        print(*res[::-1])
        break