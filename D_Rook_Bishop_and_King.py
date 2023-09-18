import math


r, c, r1, c1 = list(map(int, input().split()))

reoc = 2
if r == r1 or c == c1:
    reoc = 1


def color(r, c):
    return (r % 2 == 0 and c % 2 == 1) or (r % 2 == 1 and c % 2 == 0)
if r + c == r1 + c1 or r - c == r1 - c1:
    b = 1
elif color(r, c) == color(r1, c1):
    b = 2
else:
    b = 0

print(reoc, b, min(abs(r1 - r), abs(c1 - c)) + abs(abs(r1 - r) - abs(c1 - c)))