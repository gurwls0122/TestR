import sys
dp = [1,2,4]
for i in range(3, 12):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n-1])