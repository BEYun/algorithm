import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]
for i in range(n-1):
    dp.append(max(a[i+1], dp[i] + a[i+1]))

print(max(dp))