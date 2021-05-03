import sys
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
tmp, ans = 0, 0
for i in range(N):
    tmp += time[i]
    ans += tmp

print(ans)