import sys

def push(item):
    stack.append(item)
# X를 스택에 삽입

def pop():
    if len(stack) != 0:
        print(stack[-1])
        del stack[-1]
    else:
        print("-1")
# 가장 위에 있는 정수를 빼고 출력, 없으면 -1 출력

def size():
    print(len(stack))
# 스택에 들어있는 정수의 개수 출력

def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")
# 스택이 비어있으면 1, 아니면 0 출력

def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print("-1")
# 스택의 가장 위에 있는 정수를 출력, 없으면 -1 출력

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()
    else:
        print("잘못된 명령어입니다.")