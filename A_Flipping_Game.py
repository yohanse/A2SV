res = []
def divide(l, r):
    if l > r:
        return

    mid = (l + r + 1) // 2
    res.append(mid)
    divide(mid + 1, r)
    divide(l, mid - 1)
    
divide(1, 4)
print(res)