n = int(input())
mati = list(map(int, input().split()))
lbsa = list(map(int, input().split()))
mati.sort()
lbsa.sort()
lb, ma = 0, 0
c = 0
while ma < n and lb < n:
    if mati[ma] <= lbsa[lb]:
        ma += 1
        lb += 1
        c += 1
    else:
        lb += 1

print((n - c) // 2 + (n - c) % 2)