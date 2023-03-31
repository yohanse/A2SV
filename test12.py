n, start = 15, 25
N = 2 ** n
seen =  1 << start
dp = {}

def recursive(ans, leng, seen):
    if leng == N:
        temp = ans[-1] ^ ans[0]
        if temp.bit_count() == 1:
            return ans.copy()
        return False

    if leng > 1:
        temp = ans[-1] ^ ans[-2]
        if temp.bit_count() != 1:
            return False



    for i in range(N):
        j = i.bit_count()
        if not ((seen >> i) & 1) and (seen, j) not in dp:
            seen = seen | (1 << i)
            ans.append(i)
            j = i.bit_count()
            dp[(seen, j)] = recursive(ans, leng + 1, seen)

            if dp[(seen, j)] != False:
                return dp[(seen, j)]

            ans.pop()
            seen = seen & (~(1 << i))


print(recursive([start], 1, seen))