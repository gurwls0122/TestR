import sys
n = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][j+1]
        else:
            if i==1:
                dp[i][j] = 1
            else:
                if j==9:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)