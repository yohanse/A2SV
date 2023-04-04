start_row, start_col, end_row, end_col = list(map(int, input().split()))

# rock

if start_row == end_row or start_col == end_col:
    print(1, end = " ")
else:
    print(2, end = " ")

# bishop

if (start_row + start_col) % 2 != (end_row + end_col) % 2:
    print(0, end = " ")
elif start_col + start_row == end_row + end_col:
    print(1, end = " ")
elif start_col - start_row == end_col - end_row:
    print(1, end = " ")
else:
    print(2, end = " ")


print(max(abs(start_row - end_row), abs(start_col - end_col)))