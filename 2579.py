import sys
lst = []
d = [0] * 300
N = int(sys.stdin.readline())
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))
for i in range(N):
    if i == 0:
        d[i] = lst[i]
    elif i == 1:
        d[i] = lst[i-1]+lst[i]
    elif i==2:
        d[i] = max(lst[i-2]+lst[i], lst[i-1]+lst[i])
    else:
        d[i] = max(d[i-2] + lst[i], d[i-3] +lst[i-1]+lst[i])
print(d[N-1])