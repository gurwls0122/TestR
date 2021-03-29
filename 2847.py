import sys
lst = []
ans = 0
N = int(sys.stdin.readline())
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

for i in range(N-2, -1, -1):
    if lst[i] >= lst[i+1]:
        ans += lst[i]-lst[i+1] + 1
        lst[i] = lst[i+1]-1
    else:
        continue
print(ans)