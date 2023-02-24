n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
a.sort()
b.sort()
for i in range(n):
    for j in range(n):
        if i != j and a[i] + a[j] > b[i] + b[j]:
            c += 1
print(c//2)