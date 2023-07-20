import sys
input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

ans = []
n = int(input())
nums = list(map(int, input().split()))
x = 0
for i in range(n):
    if nums[i] == 1:
        x += 1

primes = []
limit = 2 * n + 1
for i in range(2, limit):
    if isPrime(i):
        primes.append(i)




y = n - x
count = i = 0
while x > 0 and y > 0:
    if primes[i] - count > 1:
        count += 2
        ans.append(2)
        y -= 1
            
    elif primes[i] - count > 0:
        count += 1
        ans.append(1)
        x -= 1

    else:
        i += 1
        if i == len(primes):
            break

while x:
    ans.append(1)
    x -= 1

while y:
    ans.append(2)
    y -= 1

print(*ans)