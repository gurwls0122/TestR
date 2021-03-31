import sys
T = int(sys.stdin.readline())
for _ in range(T):
    ans = 0
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    max = price[-1]
    for i in range(N-2, -1, -1):
        if price[i] < max:
            ans+= max - price[i]
        else:
            max = price[i]
    print(ans)