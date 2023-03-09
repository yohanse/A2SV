n = int(input())
food = input().split()
index, answer = 0, 0

while index < n:
    first = index
    
    while index < n and food[index] == food[first]:
        index += 1

    middle = index
    while index < n and food[first] != food[index]:
        index += 1

    last = index

    answer = max(answer, 2 * min(middle - first, last - middle))
    index = middle
print(answer)
