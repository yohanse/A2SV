import sys

"""- (A, B): -1
- (A, C): 4
- (B, C): 3
- (B, D): 2
- (B, E): 2
- (D, B): 1
- (D, C): 5
- (E, D): -3"""

dis = {}

edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3,], [1, 3, 2], [1, 4, 2], ]
for i in range(5):
    for a, b, c in edges:
        dis[b] = min(dis.get(b, sys.maxsize), dis.get(b, sys.maxsize) + c)
    print(dis)

