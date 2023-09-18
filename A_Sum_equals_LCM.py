t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for i in range(2, int(n ** 0.5) + 2):
        flag = 0
        while n % i == 0:
            n //= i
            flag = 1
        count += flag
    if n != 1:
        count += 1
    
    if count < 2:
        print("No")
    else:
        print("Yes")