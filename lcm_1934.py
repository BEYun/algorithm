import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    A, B = a, b
    while a != 0:
        b = b % a
        a, b = b, a
    print(A * B // b)