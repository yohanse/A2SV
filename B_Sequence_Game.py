t = int(input())

for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))

    ans = [num[0]]

    for i in range(1, n):
        if num[i] > num[i - 1]:
            ans.append(num[i])
        else:
            if num[i] == 1:
                if ans[-1] != 1:
                    ans.append(1)
                ans.append(1)
            else:
                ans.append(num[i] - 1)
                ans.append(num[i])
    print(len(ans))
    print(*ans)