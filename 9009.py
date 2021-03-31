import sys
T = int(sys.stdin.readline())
fib = [0, 1]
for i in range(2, 46):
    fib.append(fib[i-1]+fib[i-2])
for _ in range(T):
    i = 1
    ans = []
    n = int(sys.stdin.readline())
    while n!=0:
        if fib[i] > n:
            ans.append(fib[i-1])
            n = n - fib[i-1]
            i = 1
        else:
            i= i+1
            continue
    ans.sort()
    print(" ".join(map(str, ans)))