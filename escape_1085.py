import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
x_out = w-x
y_out = h-y
print(min(x, y, x_out, y_out))