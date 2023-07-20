n, c = list(map(int, input().split()))
time = list(map(int, input().split()))

count = 1
for i in range(1, n):
    if time[i] - time[i - 1] > c:
        count = 0
    count += 1
print(count)