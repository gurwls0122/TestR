import sys
T = int(sys.stdin.readline())
d=[(1,0),(0,1)]
for _ in range(T):
    N = int(sys.stdin.readline())
    if N > len(d)-1:
        for i in range(len(d), N+1):
            d.append((d[i-2][0]+d[i-1][0], d[i-2][1]+ d[i-1][1]))
    print(" ".join(map(str, d[N])))