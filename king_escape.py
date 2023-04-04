n = int(input())
queen_x, queen_y = list(map(int, input().split()))
king_x, king_y = list(map(int, input().split()))
final_x, final_y = list(map(int, input().split()))

queen_x -= 1
queen_y -= 1
king_x -= 1
king_y -= 1
final_x -= 1
final_y -= 1


all_triangle = [[(queen_x, queen_y), (queen_x, 0), (queen_x + queen_y, 0)],
                [(queen_x, queen_y), (queen_x, n - 1), (queen_x + queen_y + 1 - n, n - 1)],
                [(queen_x, queen_y), (n - 1, queen_y), (n - 1, queen_x + queen_y + 1 - n)],
                [(queen_x, queen_y), (0, queen_y), (0, queen_x + queen_y)],
                [(queen_x, queen_y), (queen_x, 0), (queen_x - queen_y, 0)],
                [(queen_x, queen_y), (queen_x, n - 1), (queen_x + n - 1 - queen_y, 0)],
                [(queen_x, queen_y), (0, queen_y), (0, queen_y - queen_x)],
                [(queen_x, queen_y), (n - 1, queen_y), (n + queen_y - queen_x - 1)]
                ]

for q, e1, e2 in all_triangle:
    x_begin, x_end = min(e1[0], e2[0]), max(e1[0], e2[0])
    y_begin, y_end = min(e1[1], q[1]), max(e1[0], e2[0])