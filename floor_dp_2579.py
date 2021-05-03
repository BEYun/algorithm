import sys
input = sys.stdin.readline
n = int(input())
floor = []
dp = []
for _ in range(n):
    floor.append(int(input()))

if n >= 1:
    dp.append(floor[0])
if n >= 2:
    dp.append(max(floor[1], floor[0] + floor[1]))
if n >= 3:
    dp.append(max(floor[0] + floor[2], floor[1] + floor[2]))
    for i in range(3, n):
        dp.append(max(dp[i-2] + floor[i], dp[i-3] + floor[i-1] + floor[i]))

print(dp[-1])
