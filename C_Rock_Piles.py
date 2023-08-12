t = int(input()) # number of test case
for _ in range(t):
    a, b = list(map(int, input().split())) # number of rocks on the piles
    if a % 2 == b % 2 == 0:  # check both of the pile rocks are even or not
        print("abdullah")
    else:
        print("hasan")