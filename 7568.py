import sys

n = int(sys.stdin.readline())
body_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rank_list = []
for i in range(n):
    rank = 1
    for j in range(n):
        if body_list[i][0] < body_list[j][0] and body_list[i][1] < body_list[j][1]:
            rank += 1
    rank_list.append(rank)

for i in rank_list:
    print(i, end=' ')