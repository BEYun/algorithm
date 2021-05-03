import sys
from collections import deque

input = sys.stdin.readline
word = deque(map(str, input().rstrip()))
M = int(input())
tmp = deque()

for _ in range(M):
    com = list(map(str, input().split()))
    if com[0] == 'L':
        if word:
            tmp.appendleft(word.pop())
    elif com[0] == 'D':
        if tmp:
            word.append(tmp.popleft())
    elif com[0] == 'B':
        if word:
            word.pop()
    elif com[0] == 'P':
        word.append(com[1])

while tmp:
    word.append(tmp.popleft())
print(''.join(word))