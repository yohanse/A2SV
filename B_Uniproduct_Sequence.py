n = int(input())
num = list(map(int, input().split()))
pos, neg = 0, 0
pos_sum , neg_sum = 0, 0
zero = 0
for i in num:
    if i > 0:
        pos += 1 
        pos_sum += i - 1
    elif i < 0:
        neg += 1
        neg_sum += abs(i + 1)
    else:
        zero += 1
tot = pos_sum + neg_sum + zero
if neg % 2 == 1 and zero == 0:
    tot += 2
print(tot)

