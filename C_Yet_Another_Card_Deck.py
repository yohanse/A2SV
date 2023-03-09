n, q = list(map(int, input().split()))
card = list(map(int, input().split()))
querie = list(map(int, input().split()))
dic = {}
for i, color in enumerate(card):
    if color not in dic:
        dic[color] = i + 1

for color in querie:
    print(dic[color], end = " ")

    for i in dic:
        if dic[color] > dic[i]:
            dic[i] += 1
    dic[color] = 1