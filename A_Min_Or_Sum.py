t  = int(input())

# Processing each test case
for _ in range(t):

    # Reading size of the array
    n = int(input())

    # Reading elements of the array
    a = list(map(int, input().split()))

    min_sum = 0 # Begin by initializing a variable where none of the bits are set to one.

    # To determine the result of performing a bitwise OR operation on the entire array.
    for i in a:
        # Perform a bitwise operation using the variable min_sum.
        min_sum |= i 

    print(min_sum)