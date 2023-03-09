from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    string = input()

    def valid(l, r, lead):
        left = string[l:r + 1]
        count = Counter(left)
        return r - l + 1 - count.get(lead, 0)
    def divide(l, r, lead, n):
        if l == r:
            return valid(l, r, lead)
        
        nextlead = chr(ord(lead) + 1)
        mid = (l + r + 1) // 2
        return min(valid(mid, r, lead) + divide(l, mid - 1, nextlead, n // 2),
                    valid(l, mid - 1, lead) + divide(mid, r, nextlead, n // 2))
    print(divide(0, n - 1, 'a', n))
