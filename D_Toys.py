n, m = list(map(int, input().split()))
price = list(map(int, input().split()))
dic = {}
num = []
for i in range(m):
    z = input()
    dic[z] = 1 + dic.get(z, 0)
for i in dic:
    num.append(dic[i])
price.sort()
num.sort(reverse=True)
ans, ans1 = 0, 0

for i in range(len(num)):
    ans += num[i] * price[i]

price.sort(reverse = True)
num.sort(reverse = True)

for i in range(len(num)):
    ans1 += num[i] * price[i]

print(ans,ans1)
