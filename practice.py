import sys, heapq

input = sys.stdin.readline
N = int(input())
heap_first = []
heap_second = []

for _ in range(N):
    x = int(input())
    if len(heap_first) <= len(heap_second):
        heapq.heappush(heap_first, (-x, x))
    else:
        heapq.heappush(heap_second, (x, x))

    if heap_first and heap_second:
        if heap_first[0][1] > heap_second[0][0]:
            a = heapq.heappop(heap_second)[0]
            b = heapq.heappop(heap_first)[1]
            heapq.heappush(heap_first, (-a, a))
            heapq.heappush(heap_second, (b, b))

    print(heap_first[0][1])

