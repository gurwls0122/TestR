import sys
dp =[0]
lst = [0]
N = int(sys.stdin.readline())
lst += list(map(int, sys.stdin.readline().split()))
dp.append(lst[1])
dp.append(max(lst[2], dp[1]*2))
for i in range(3, N+1):
    dp.append(lst[i])
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp)