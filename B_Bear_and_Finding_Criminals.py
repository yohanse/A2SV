n, l = list(map(int, input().split()))
arr = list(map(int, input().split()))
c = 1
l -= 1
count = 0
while l - c > -1 and l + c < n:
    if arr[l - c] == arr[l + c] == 1:
        count += 2
    c += 1

while l - c > -1:
    count += arr[l - c]
    c += 1

while l + c < n:
    count += arr[l + c]
    c += 1

print(count + arr[l])