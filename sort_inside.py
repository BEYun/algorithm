import sys

n = int(sys.stdin.readline())
arr = []
arr = list(map(int, str(n)))
arr.sort(reverse=True)

for i in arr:
    print(i, end="")