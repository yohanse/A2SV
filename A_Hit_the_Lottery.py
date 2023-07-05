n = int(input())
min_bills = (n // 100) + ((n % 100) // 20) + (((n % 100) % 20) // 10) + ((((n % 100) % 20) % 10) // 5) + (((((n % 100) % 20) % 10) % 5))
print(min_bills)

def func():
    i = 6754
    x = str(i)[-3:] + str(i)[:-3]
    print(i, x)
    if int(x) == 2 * i:
        return i
print(func())