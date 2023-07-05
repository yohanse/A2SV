import sys, threading

def main():

    n = int(input())
    height1 = list(map(int, input().split()))
    height2 = list(map(int, input().split()))
    arr = [height1, height2]
    memo = {}
    def dp(index, row):
        if index == n:
            return 0
        if (row, index) in memo:
            return memo[(row, index)]
        memo[(row, index)] = max(dp(index + 1, 1 - row) + arr[row][index], dp(index + 1, row))
        return memo[(row, index)]

    print(max(dp(0, 0), dp(0, 1)))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()

