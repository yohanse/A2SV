n = int(input())
num = list(map(int, input().split()))
for i in num:
    if i%2 == 1:
        num.sort()
        num = list(map(str,num))
        print(" ".join(num))
        break
else:
    num = list(map(str,num))
    print(" ".join(num))