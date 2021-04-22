import sys
lst = [0]
dp = []
n = int(sys.stdin.readline())
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for i in range(n+1):
    if i == 0 or i==1:
        dp.append(lst[i])
    elif i==2:
        dp.append(dp[1] + lst[i])
    else:
        dp.append(max(dp[i-2]+lst[i], dp[i-3] + lst[i-1] + lst[i], dp[i-1]))
print(dp[n])