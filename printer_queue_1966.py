import sys

test_n = int(sys.stdin.readline())

for _ in range(test_n):
    N, M = map(int, sys.stdin.readline().split())
    point = list(map(int, sys.stdin.readline().split()))
    index = [0 for i in range(N)]
    index[M] = 1
    cnt = 0
    while True:
        if point[0] == max(point):
            cnt += 1
            if index[0] == 1:
                print(cnt)
                break
            else:
                point.pop(0)
                index.pop(0)

        else:
            point.append(point.pop(0))
            index.append(index.pop(0))