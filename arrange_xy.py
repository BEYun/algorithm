import sys

n = int(sys.stdin.readline())
xy_arr = []

for _ in range(n):
    xy_arr.append(list(map(int,input().split())))

xy_arr.sort(key=lambda x : (x[1], x[0]))

for i in range(n):
    print(xy_arr[i][0], xy_arr[i][1])

