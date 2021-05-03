import sys
input = sys.stdin.readline
n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)
dp = [0] * n

if t[n-1] == 1:
    dp[n-1] = p[n-1]

for i in range(n-2, -1, -1):
    if i + t[i] == n:
        dp[i] = max(p[i], dp[i+1])
    elif i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i+t[i]], dp[i+1])

print(dp[0])