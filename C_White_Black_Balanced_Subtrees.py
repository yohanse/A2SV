import sys, threading

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        color = input()
        graph = [[] for i in range(n)]

        for i in range(n - 1):
            graph[arr[i] - 1].append(i + 1)

        def post(vertex):
            if graph[vertex] == []:
                return -1 if color[vertex] == 'B' else 1, 0
            count = -1 if color[vertex] == 'B' else 1
            ans = 0
            for adj in graph[vertex]:
                c, a = post(adj)
                count += c
                ans += a
            if count == 0:
                ans += 1
            return count, ans
        print(post(0)[1])

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()