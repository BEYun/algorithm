import sys
money = int(sys.stdin.readline())
arr = [500, 100, 50, 10, 5, 1]
change = 1000 - money
cnt = 0
for i in range(len(arr)):
    while change - arr[i] >= 0:
        change -= arr[i]
        cnt += 1
    if change == 0:
        break

print(cnt)