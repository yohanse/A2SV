n, m, k = list(map(int, input().split()))
num = list(map(int, input().split()))

num.sort(reverse = True)
if k == m:
    print(num[0] * k)
else:
    second = m // (k + 1)
    first = (m % (k + 1))
    print(second * num[0] * k + num[0] * first + second*num[1])
   