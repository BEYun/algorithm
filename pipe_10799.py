import sys
from collections import deque
pipe = sys.stdin.readline().rstrip()
pipe = deque(pipe)
stack = []
stack.append(pipe.popleft())
cnt = 0

while pipe:
    tmp = pipe.popleft()
    if tmp == '(':
        stack.append(tmp)
    else:
        stack.pop()
        cnt += len(stack)
        while pipe:
            tmp = pipe.popleft()
            if tmp == '(':
                stack.append(tmp)
                break
            else:
                stack.pop()
                cnt += 1

print(cnt)