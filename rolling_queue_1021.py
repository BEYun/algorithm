import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
n_list = deque([i+1 for i in range(N)])
a_list = deque(map(int, sys.stdin.readline().split()))
cnt = 0

while a_list:
    if n_list[0] == a_list[0]:
        n_list.popleft()
        a_list.popleft()

    elif n_list.index(a_list[0]) <= len(n_list) // 2:
        n_list.append(n_list.popleft())
        cnt += 1

    elif n_list.index(a_list[0]) > len(n_list) // 2:
        n_list.appendleft(n_list.pop())
        cnt += 1

print(cnt)
