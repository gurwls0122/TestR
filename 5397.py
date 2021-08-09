n = int(input())
for _ in range(n):
    key = input()
    left = []
    right = []
    for word in key:
        if word == '-':
            if left:
                left.pop()
        elif word == '<':
            if left:
                right.append(left.pop())
        elif word == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(word)

    while right:
        left.append(right.pop())
    print(''.join(left))