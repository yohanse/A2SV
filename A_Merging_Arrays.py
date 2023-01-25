n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
res = [0]*(n+m)
i, j, k = 0, 0, 0

while i < n and j < m:
    if arr[i] < arr1[j]:
        res[k] = arr[i]
        i += 1
    else:
        res[k] = arr1[j]
        j += 1
    k += 1

while i < n:
    res[k] = arr[i]
    i += 1
    k += 1

while j < m:
    res[k] = arr1[j]
    j += 1
    k += 1

for i in res:
    print(i, end = " ")
