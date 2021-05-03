import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n+1)])
cnt = 0
answer = []
while queue:
    if cnt == k-1:
        answer.append(queue.popleft())
        cnt = 0
    else:
        queue.append(queue.popleft())
        cnt += 1
if len(answer) == 1:
    print('<%d>'%answer[0])
else:
    for i in range(n):
        if i == 0:
            print('<%d, '%answer[i], end='')
        elif i == n-1:
            print('%d>'%answer[i], end='')
        else:
            print('%d, '%answer[i], end='')
