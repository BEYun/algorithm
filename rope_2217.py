import sys
n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)
max_w = 0
for i in range(1, n+1):
    max_w = max(max_w, rope[i-1] * i)
print(max_w)
