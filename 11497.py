import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    ans = 0
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    for i in range(N-2):
        ans = max(ans, abs(L[i]-L[i+2]))
    print(ans)
