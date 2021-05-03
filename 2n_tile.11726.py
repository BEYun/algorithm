import sys
input = sys.stdin.readline
dp = [1, 2]
for i in range(2, 1001):
    dp.append(dp[i-2] + dp[i-1])

n = int(input())
print(dp[n-1] % 10007)