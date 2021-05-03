import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque([])

for _ in range(N):
    com = list(map(str, sys.stdin.readline().split()))
    if com[0] == 'push_front':
        deq.appendleft(com[1])
    elif com[0] == 'push_back':
        deq.append(com[1])
    elif com[0] == 'pop_front':
        if not deq:
            print('-1')
        else:
            print(deq.popleft())
    elif com[0] == 'pop_back':
        if not deq:
            print('-1')
        else:
            print(deq.pop())
    elif com[0] == 'size':
        print(len(deq))
    elif com[0] == 'empty':
        if not deq:
            print('1')
        else:
            print('0')
    elif com[0] == 'front':
        if not deq:
            print('-1')
        else:
            print(deq[0])
    elif com[0] == 'back':
        if not deq:
            print('-1')
        else:
            print(deq[-1])