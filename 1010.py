import sys
d = [[0 for _ in range(30)] for _ in range(30)]
T = int(sys.stdin.readline())
def c_b(n, m):
    if d[n][m] !=0:
        return d[n][m]
    elif n==m:
        return 1
    elif n==1:
        return m
    else:
        d[n][m] = c_b(n,m-1) + c_b(n-1,m-1)
    return d[n][m]
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(c_b(N,M))