import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [[0, 0]]
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if a[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i][0]] + a[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])