import sys

n, m = map(int, sys.stdin.readline().split())
chess = []
min_cnt = []
for _ in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        cnt_w, cnt_b = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != 'W':
                        cnt_w += 1
                    if chess[k][l] != 'B':
                        cnt_b += 1
                else:
                    if chess[k][l] != 'B':
                        cnt_w += 1
                    if chess[k][l] != 'W':
                        cnt_b += 1
        min_cnt.append(cnt_w)
        min_cnt.append(cnt_b)

print(min(min_cnt))