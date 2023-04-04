word = list(input())

maxi = max(word)
pointer = 0
for i in range(len(word)):
    if maxi == word[i]:
        pointer += 1

print(maxi * pointer)