import sys
input = sys.stdin.readline
dp = [1, 2, 4]
for i in range(3, 11):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

n = int(input())
for _ in range(n):
    k = int(input())
    print(dp[k-1])