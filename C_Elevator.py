t = int(input())
for _ in range(t):
    Wt, Et, Ef = list(map(int, input().split()))
    elvator = (Ef + 4) *Et
    walk = 4 * Wt
    walk_elavator = (Wt * Ef) + ((4 - Ef) * Et)
    print(min(elvator, walk, walk_elavator))