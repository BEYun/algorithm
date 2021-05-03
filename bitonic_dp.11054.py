import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp_inc = [1] * n
dp_dec = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp_inc[i]+dp_dec[i]-1)

print(answer)