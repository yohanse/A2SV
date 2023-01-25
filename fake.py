n = int(input())
num = list(map(int, input().split()))
i = 1
count = 0
while i < n:
    if num[i - 1] >= num[i]:
        initial = i - 1
        while i < n and num[i-1] > num[i]:
            i += 1 
        final = i - 1
        count += 1
    i += 1
if count == 0:
    print("yes")
    print(1, 1)
elif count == 1:
    p1, p2 = final, initial
    while initial < final:
        num[initial], num[final] = num[final], num[initial]
        final -= 1
        initial += 1
    for i in range(1,n):
        if num[i] < num[i-1]:
            print("no")
            break
    else:
        print("yes")
        print(p1, p2)
else:
    print("no")