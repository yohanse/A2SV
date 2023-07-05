import sys, threading

def main():

    n = int(input())
    num = list(map(int, input().split()))

    memo = {}
    def dp(index, previous):
        if index == n:
            return 0
        if (index, previous) in memo:
            return memo[(index, previous)]
        memo[(index, previous)] = dp(index + 1, -1) + 1
        if num[index] == 3:
            if previous != 1:
                memo[(index, previous)] = min(memo[(index, previous)], dp(index + 1, 1))
            if previous != 2:
                memo[(index, previous)] = min(memo[(index, previous)], dp(index + 1, 2))
            

        if num[index] == 1 and previous != 1:
            memo[(index, previous)] = min(memo[(index, previous)], dp(index + 1, 1))
            
        if num[index] == 2 and previous != 2:
            memo[(index, previous)] = min(memo[(index, previous)], dp(index + 1, 2))
        
        return memo[(index, previous)]

    print(dp(0, -1))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()




