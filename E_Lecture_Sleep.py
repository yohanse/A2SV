n, k = list(map(int,input().split()))
te = list(map(int,input().split()))
st = list(map(int,input().split()))
ans,tot = 0 ,0
for r in range(n):
    if st[r] == 0:
        tot += te[r]
    ans = max(ans,tot)
    if r>=k-1:
        if st[r-k + 1] == 0:
            tot -= te[r-k +1]
tot =0
for i in range(n):
    if st[i] == 1:
        tot += te[i]
print(ans+tot)