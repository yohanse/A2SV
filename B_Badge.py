n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    visite = set()
    while i not in visite:
        visite.add(i)
        i = nums[i] - 1
    print(i + 1, end = " ")