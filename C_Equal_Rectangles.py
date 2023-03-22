from collections import Counter
q = int(input())
for _ in range(q):
    n = int(input())
    num = list(map(int, input().split()))
    count = Counter(num)
    arr = []

    for i in count:
        arr.append((i, count[i]))

    arr.sort()
    l, r = 0, len(arr) - 1
    if len(arr) == 1:
        print("YES")
    
    else:

        area = arr[0][0] * arr[-1][0]
        while l < r:
            if area != (arr[l][0] * arr[r][0]) or arr[l][1] != arr[r][1] or (arr[l][1] + arr[r][1]) % 4!= 0 or arr[l][1] % 2 != 0:
                print("NO")
                break
            l += 1
            r -= 1
        else:
            if l == r:
                if arr[l][1] % 4 != 0 or arr[l][0] ** 2 != area:
                    print("NO")
                else:
                    print("YES")
            else:
                print("YES")