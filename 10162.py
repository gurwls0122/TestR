import sys
T = int(sys.stdin.readline())
sec = [300, 60, 10]
ans = []
for i in sec:
    if T >= i:
        ans.append(T//i)
        T = T % i
    else:
        ans.append(0)
if T!=0:
    print(-1)
else:
    print(' '.join(map(str,ans)))