matrial = input()
have = list(map(int, input().split()))
price = list(map(int, input().split()))
money = int(input())

count = {'B':0, 'S':0, 'C':0}

for i in matrial:
    count[i] += 1

l, r = 0, max(have) + money

while l < r:
    mid = (l + r + 1) // 2
    need = 0
    inger = "BSC"
    for i in range(3):
        if have[i] - count[inger[i]] * mid < 0:
            need += (count[inger[i]] * mid - have[i]) * price[i]
    if money < need:
        r = mid - 1
    else:
        l = mid
print(l)