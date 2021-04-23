import sys
n = int(sys.stdin.readline())
dp = [[0]*n for _ in range(n)]
lst= [[0] for _ in range(n)]
for i in range(n):
    inp = list(map(int, sys.stdin.readline().split()))
    lst[i] = inp

for i in range(n):
    for j in range(len(lst[i])):
        if i==0:
            dp[i][j] = lst[i][j]
        else:
            if j==0:
                dp[i][j] = dp[i-1][j]+ lst[i][j]
            elif j == len(lst[i])-1:
                dp[i][j]=dp[i-1][j-1] + lst[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1], dp[i-1][j]) + lst[i][j]
print(max(dp[n-1]))
print(dp)