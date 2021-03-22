import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    com = sys.stdin.readline().strip().split()
    command = com[0]
    if command == "push":
        stack.append(com[1])
    elif command == "top":
        if stack == []:
            print("-1")
        else:
            print(stack[-1])
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack == []:
            print("1")
        else:
            print("0")
    elif command == "pop":
        if stack == []:
            print("-1")
        else:
            print(stack.pop())