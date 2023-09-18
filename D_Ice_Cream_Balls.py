from decimal import Decimal, getcontext

getcontext().prec = 100  # Setting precision. You can increase this if needed.

t = int(input())
for _ in range(t):
    x = Decimal(input())

    ans = (Decimal(0.25) + 2 * x).sqrt()
    ans += Decimal(0.5)
    ans = ans.to_integral_value(rounding='ROUND_CEILING')  # Equivalent to math.ceil for Decimals

    c = (ans * (ans - 1)) / 2
    if int(c) == x:
        print(int(ans))
    else:
        ans -= 1
        z = (ans * (ans - 1)) / 2
        print(int(ans + x - z))
