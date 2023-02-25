n, m = list(map(int, input().split()))
remain = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = [0] * n

for i in range(n):
    total[i] = [cost[i], remain[i], i]

total.sort()

dic = {}

for i in range(n):
    dic[total[i][2]] = i

l = 0
for i in range(m):
    kind, number = list(map(int, input().split()))
    kind = dic[kind - 1]
    print(total[kind])

    if total[kind][1] -  number < 0:
        answer = total[kind][1] * total[kind][0]
        print(answer)
        number -= total[kind][1]
        total[kind][1] = 0
        print(total[l])
        while l < n and total[l][1] - number < 0:
            answer += total[l][1] * total[l][0]
            print(total[l][1] * total[l][0])
            number -= total[l][1]
            total[l][1] = 0
            l += 1
            print(total[l])
        answer += number * total[kind][0]
        total[kind][1] -= number
    else:
        answer = number * total[kind][0]
        total[kind][1] -= number
    print(answer)


