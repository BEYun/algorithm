import sys
dp = [0, 1, 1]
for i in range(3, 91):
    dp.append(dp[i-2] + dp[i-1])

n = int(sys.stdin.readline())
print(dp[n])