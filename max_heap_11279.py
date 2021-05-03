import sys
import heapq

input = sys.stdin.readline
N = int(input())
max_heap = []

for _ in range(N):
    k = int(input())
    if k == 0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print('0')
    else:
        heapq.heappush(max_heap, (-k, k))