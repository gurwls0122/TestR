import sys
lst=[]
d=[0]*16
N = int(sys.stdin.readline())
for _ in range(N):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(N-1, -1, -1):
    if i+lst[i][0] > N:
        d[i] = d[i+1]
        continue
    else:
        d[i] =  max(d[i+lst[i][0]] + lst[i][1], d[i+1])

print(d)
