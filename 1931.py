import sys
N = int(sys.stdin.readline())
time_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_list.sort(key=lambda x:(x[1], x[0]))
cnt = 1
end = time_list[0][1]

for i in range(1, N):
    if time_list[i][0] >= end:
        cnt += 1
        end = time_list[i][1]

print(cnt)