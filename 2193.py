import sys
d=[1,1]
N = int(sys.stdin.readline())
for i in range(2, N):
    d.append(d[i-1]+d[i-2])
print(d[N-1])