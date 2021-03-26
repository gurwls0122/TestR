import sys
now_loc = 0
count = 0
N,L = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort()

for i in range(N):
    if now_loc < leak[i]:
        count+=1
        now_loc = leak[i] + (L-0.5)
    else:
        continue
print(count)