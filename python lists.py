if __name__ == '__main__':
    N = int(input())
    a = []
    for _ in range(N):
        command = input()
        if command[:6] == 'append':
            a.append(int(command[7:]))
        elif command == 'print':
            print(a)
        elif command[:6] == 'remove':
            a.remove(int(command[7:]))
        elif command[:6] == 'insert':
            i, e = command[7:].split()
            a.insert(int(i),int(e))
        elif command == 'sort':
            a.sort()
        elif command == 'pop':
            a.pop()
        else:
            a.reverse()   