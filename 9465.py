import sys
T = int(sys.stdin.readline())
for _ in range(T):
    lst = []
    n = int(sys.stdin.readline())
    lst.append(list(map(int, sys.stdin.readline().split())))
    lst.append(list(map(int, sys.stdin.readline().split())))

    lst[0][1] += lst[1][0]
    lst[1][1] += lst[0][0]

    for i in range(2, n):
        lst[0][i] += max(lst[1][i-1], lst[1][i-2])
        lst[1][i] += max(lst[0][i-1], lst[0][i-2])

    print(lst)
    print(max(lst[0][n-1],lst[1][n-1]))