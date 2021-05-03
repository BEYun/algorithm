import sys

def insert(item):
    stack.append(item)

def del_item():
    if len(stack) > 0:
        del stack[-1]

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    ps = list(map(str,sys.stdin.readline().strip()))
    for i in range(len(ps)):
        if ps[i] == "(":
            insert("(")
        elif ps[i] == ")":
            if len(stack) == 0:
                stack.append("NO")
                break
            else:
                del_item()
    if len(stack) == 0:
        print("YES")
    elif stack[-1] == "NO" or len(stack) > 0:
        print("NO")