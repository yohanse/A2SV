def smallest_cost(n):
    # Calculate the highest power of 2 less than n
    k = 1
    while (1 << k) <= n:
        k += 1
    k -= 1

    # Generate a Gray code sequence of length k
    gray_code = [0]
    for i in range(k):
        gray_code += [x + (1 << i) for x in reversed(gray_code)]

    # Construct the sequence of heights using the Gray code sequence
    heights = [gray_code[i] for i in range(k + 1)]
    for i in range(k + 1, n):
        heights.append(heights[-1] ^ (heights[-1] & -heights[-1]) << 1)

    return heights

t = int(input())
for i in range(t):
    n = int(input())
    p = smallest_cost(n)
    print(*p)