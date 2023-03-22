n = int(input())
num = 1
ans = 0
stack = [0  for i in range(100000)]
pointer = 0
for i in range(n):
    command = input()
    if command == "add":
        if ans + num > 2**32 - 1:
            print("OVERFLOW!!!")
            ans += num
            break
        ans += num

    elif command == "end":
        if pointer == 0:
            num = 1
            
        else:
            num = stack[pointer - 1]
            pointer -= 1
    else:
        stack[pointer] = num
        num *= int(command[4:])
        pointer += 1
    
    
    

if ans <= 2**32 - 1:

    print(ans)