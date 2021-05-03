import sys

def insert(item):
    stack.append(item)

def del_item():
    del stack[-1]

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        del_item()
    else:
        insert(int(command))

print(sum(stack))