t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    num = list(map(int, list(input())))
    res = [-1]*n
    res1 = [-1] * n
    curr = -1
    for i in range(n):
        if num[i] == 1:
            res[i] = i
            curr = i
        else:
            res[i] = curr

    curr = -1
    for i in range(n- 1, -1, -1):
        if num[i] == 1:
            res1[i] = i
            curr = i
        else:
            res1[i] = curr

    
    answer = [0]*n
    for i in range(n):
        if res[i] == -1 and res1[i] != -1 and res1[i] - i <= m:
            answer[i] = 1
        elif res1[i] == -1 and res[i] != -1 and i - res[i] <= m:
            answer[i] = 1
        elif  res[i] != -1 and res1[i] != -1 and i - res[i] != res1[i] - i and (i - res[i] <= m or  res1[i] - i <= m):
            answer[i] = 1

    for i in range(n):
        if num[i]:
            answer[i] = 1


    
    print(''.join(list(map(str, answer))))