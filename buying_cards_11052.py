import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
dp[1] = cards[0]
dp[2] = max(cards[1], dp[1] * 2)

for i in range(3, n+1):
    dp[i] = cards[i-1]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

print(dp[-1])
