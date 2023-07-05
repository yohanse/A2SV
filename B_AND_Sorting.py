import math

# Taking the number of test cases
t = int(input())

# Processing each test case
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    bits_needed = math.ceil(math.log2(n))
    
    max_x = 0
    for bit in range(bits_needed - 1, -1, -1):
        found = False
        mask = 1 << bit
        for i in range(n):
            if p[i] & mask:
                for j in range(n):
                    if i != j and p[j] & mask:
                        found = True
                        break
            if found:
                break
        if found:
            max_x |= mask
    
    # The maximum value of X for this test case
    print(max_x)
