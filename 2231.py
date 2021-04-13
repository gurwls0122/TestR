import sys
N = int(sys.stdin.readline())
result=0
for i in range(1, N):
    num = list(map(int, str(i)))
    if i+sum(num) == N:
        result = i
        break
print(result)