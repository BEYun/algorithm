import sys

N, M = map(int, sys.stdin.readline().split())
M_list = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if M_list[i] + M_list[j] + M_list[k] > M:
                continue
            else:
                result = max(result, M_list[i] + M_list[j] + M_list[k])

print(result)