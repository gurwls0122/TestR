import sys
T = int(sys.stdin.readline())
for _ in range(T):
    lst = []
    count = 0
    N = int(sys.stdin.readline())
    rank = N
    for _ in range(N):
        a,b = map(int, sys.stdin.readline().split())
        lst.append((a,b))
    lst.sort(key = lambda x : x[0])
    for i in range(N):
        if lst[i][1] <= rank:
            count+=1
            rank = lst[i][1]
        else:
            continue
    print(count)