t = int(input())
for _ in range(t):
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a, b, c, d = r[0], r[1], c[0], c[1]
    check = "NO"
    def chec(a, b, c, d):
        if a < b and a < c and c < d and b < d:
            return True
        return False
    if chec(a, b, c, d):
        check = "YES"
    if chec(b, d, a, c):
        check = "YES"
    if chec(d, c, b, a):
        check = "YES"
    if chec(c, a, d, b):
        check = "YES"
    print(check)
