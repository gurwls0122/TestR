import sys
d= [0] * 101
d[1] = d[2] = d[3] = 1
d[4] = d[5] = 2
lst = [[1,1], [1,2], [1,2]]
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n<=5:
        print(d[n])
    else:
        for i in range(6, n+1):
            if d[i]!=0:
                continue
            else:
                d[i] = d[i-1] + d[i-5]
        print(d[n])