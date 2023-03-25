arr = [5,1,3,4,2]

for i in range(len(arr)):
    while arr[i] - 1 != i:
        index = arr[i] - 1
        arr[i], arr[index] = arr[index], arr[i]
print(arr)