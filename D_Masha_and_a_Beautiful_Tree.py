t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))

    
    def valid(a, b):
        c = a + b
        check = True
        for i in range(1, len(c)):
            if c[i - 1] >= c[i]:
                check = False
                break
        if check:
            return 0, c
        
        c = b + a
        check = True
        for i in range(1, len(c)):
            if c[i - 1] >= c[i]:
                check = False
                break
        if check:
            return 1, c
        
        return "False", c
    num = [[i] for i in num]
    answer = 0
    check = False
    while n != 1:
        temp = [[] for i in range(n // 2)]
        
        for i in range(1, n, 2):
            # print(i, num, n)
            t = valid(num[i - 1], num[i])
            if t[0] == "False":
                check = True
            else:
                answer += t[0]
                temp[i // 2] = t[1]
        if check:
            print(-1)
            break
        num = temp
        n //= 2
    if not check:
        print(answer)