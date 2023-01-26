n = int(input())
num = list(map(int, input().split()))
check1, check2 = False, False
for i in num:
    if i%2 == 1:
        check1 = True
    else:
        check2 = True
    if check1 and check2:
        num.sort()
        num = list(map(str,num))
        print(" ".join(num))
        break 
else:
    num = list(map(str,num))
    print(" ".join(num))