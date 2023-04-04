from collections import defaultdict

n = int(input())
coordinate = []
for _ in range(n):
    coordinate.append(tuple(list(map(int, input().split()))))

horizontal = defaultdict(list)
vertical = defaultdict(list)

for x, y in coordinate:
    horizontal[x].append(y)
    vertical[y].append(x)

seen = set()
group = 0
for x,y in coordinate:
    if (x, y) not in seen:
        seen.add((x, y))
        stack = [(x, y)]
        group += 1
        while stack:
            x, y = stack.pop()

            for i in horizontal[x]:
                if (x, i) not in seen:
                    stack.append((x, i))
                    seen.add((x, i))

            for i in vertical[y]:
                if (i, y) not in seen:
                    stack.append((i, y))
                    seen.add((i, y))
            


print(group - 1)