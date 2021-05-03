import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = deque([i+1 for i in range(N)])

print('<', end='')
while arr:
    for _ in range(K-1):
        arr.append(arr[0])
        arr.popleft()
    print(arr.popleft(), end='')
    if arr:
        print(',', end=' ')
print('>', end='')
