n1 = input()
n2 = input()
n3 = input()
n1 += n2
letter = [0]*26
letter1 = [0]*26
for i in n1:
    letter[ord(i) - ord("A")] += 1
for i in n3:
    letter1[ord(i) - ord("A")] += 1
if letter1 == letter:
    print("YES")
else:
    print("NO")