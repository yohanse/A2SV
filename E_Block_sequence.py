n, m = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
r = n - 1
index = []
count = 0
for i in range(n):
    num.sort()
    maxi = num[r]
    if maxi == 0 or maxi == 1 or r < 0:
        if maxi == 1:
            count += n - r - 1
        break
    for j in range(n):
        if maxi <= num[j]:
            index.append(j)
    if len(index) > 1 and maxi != 1:
        count += len(index) - 1
    
    for j in index:
        num[j] -= 1
    index = []
    r -= 1
    
            
   
print(count)
    