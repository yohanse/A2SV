MODULO = 10**9 + 7

# Function to find the k-th special number modulo 10^9 + 7
def find_special_number(n, k):
    # Convert k to binary base and treat as a number in base n
    special_number = 0
    power_of_ten = 1
    while k:  # while k not zero
        remainder = k % 2
        # build the number in base n
        special_number = (special_number + remainder * power_of_ten) % MODULO
        power_of_ten = (power_of_ten * n) % MODULO
        k //= 2
    return special_number

# Input Reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # function call to find the special number
    print(find_special_number(n, k))