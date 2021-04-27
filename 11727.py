import sys
n = int(sys.stdin.readline())
d = [0, 1, 3, 5]
for i in range(4, n+1):
    d.append(d[i-1]+d[i-2]*2)
print(d[n]%10007)