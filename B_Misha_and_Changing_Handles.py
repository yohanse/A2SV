q = int(input())
dic = {}
can_not = set()
for i in range(q):
    a, b = input().split()
    dic[a] = b
    can_not.add(b)
ans = []
for i in dic:
    if i not in can_not:
        curr = i
        while curr in dic:
            curr = dic[curr]
        ans.append([i, curr])
print(len(ans))
for a, b in ans:
    print(a, b)
