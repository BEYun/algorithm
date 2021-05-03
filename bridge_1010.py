import sys
input = sys.stdin.readline
T = int(input())
dp = [[0]*31 for i in range(31)]
for i in range(1, 31):
    for j in range(1, i+1):
        if j == i:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M][N])