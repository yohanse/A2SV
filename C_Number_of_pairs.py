b = int(input())
boy = list(map(int, input().split()))
g = int(input())
girl = list(map(int, input().split()))

boy.sort()
girl.sort()

i, j = 0, 0
ans = 0
while i < b and j < g:
    if abs(boy[i] - girl[j]) <= 1:
        ans += 1
        i += 1
        j += 1
    elif boy[i] < girl[j]:
        i += 1
    else:
        j += 1
print(ans) 