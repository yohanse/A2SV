    


#dont pick and stay here 
import sys, threading
from functools import lru_cache
input = sys.stdin.readline


def main():
    n, l, r = list(map(int, input().split()))

    def dp(n, i = 1):
        if n < 2:
            if l <= i <= r:
                return i, n
            return i, 0
        if i > r:
            return i, 0

        il, al = dp(n // 2, i)
        if l <= il + 1 <= r:
            al += n % 2
        ir, ar = dp(n // 2, il + 2)
        return ir, ar + al

    print(dp(n)[1])


sys.setrecursionlimit( 1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()