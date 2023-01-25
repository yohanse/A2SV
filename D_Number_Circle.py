n  = int(input())
num = list(map(int, input().split()))
num.sort()
if num[-2] + num[0] > num[-1]:
    print("YES")
    num = list(map(str, num))
    num = " ".join(num)
    print(num[::-1])
else:
    print("NO")