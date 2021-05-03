import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_1, cnt_0, cnt_m1 = 0, 0, 0

def div_conq(x, y, n):
    global cnt_0, cnt_1, cnt_m1
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        div_conq(x + k * n//3, y + l * n//3, n//3)
                return
    if num == 1:
        cnt_1 += 1
    elif num == 0:
        cnt_0 += 1
    else:
        cnt_m1 += 1

div_conq(0, 0, N)
print(cnt_m1)
print(cnt_0)
print(cnt_1)