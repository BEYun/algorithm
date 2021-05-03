import sys

N = int(sys.stdin.readline())
count = 0
stack = []
result = []
no_message = True

for i in range(N):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    
    else:
        no_message = False

if no_message == False:
    print("NO")

else:
    for i in result:
        print(i)
