import sys
N = int(sys.stdin.readline())
km = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
min_cost = cost[0]
answer = 0

for i in range(N-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    answer += min_cost * km[i]

print(answer)