n, k, d = list(map(int, input().split()))

arr = [[1, 0] for i in range(n + 1)]
arr[d][1] = 1


for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i - j > -1:
            if j >= d:
            

                    
                arr[i][1] += arr[i - j][1] + arr[i - j][0]
            else:
                arr[i][0] += arr[i - j][0]
                arr[i][1] += arr[i - j][1]
        
print(arr)
print(arr[-1][1]) 