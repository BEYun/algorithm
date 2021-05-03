import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = []
    cnt = 1
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort(key=lambda x:x[0])
    min_int = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < min_int:
            cnt += 1
            min_int = arr[i][1]
    print(cnt)