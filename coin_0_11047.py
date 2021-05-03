import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
highest = N-1
coin_list = [int(sys.stdin.readline()) for _ in range(N)]

while K != 0:
    if K >= coin_list[highest]:
        cnt += K // coin_list[highest]
        K %= coin_list[highest]
    else:
        highest -= 1

print(cnt)