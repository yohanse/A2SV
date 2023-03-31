t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    num = list(map(int, input().split()))
    
    prefix = [0]
    for i in range(n):
        prefix.append(num[i] % 2 + prefix[-1])
    odd = True if prefix[-1] % 2 else False
    for i in range(q):
        s, e, k = list(map(int, input().split()))
        check = 0
        if  (e - s + 1) % 2 == 1 and k % 2 == 1:
            check = 1
        if (prefix[e] - prefix[s - 1]) % 2 != check:
            if not odd:
                print("YES")
            else:
                print("NO")
        else:
            if odd:
                print("YES")
            else:
                print("NO")