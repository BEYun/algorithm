import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) #배열
stack = [] #포인터
result = [-1 for _ in range(N)] #결과 초기값 -1

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

for i in result:
    print(i, end=" ")