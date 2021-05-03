import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(arr)/n))

# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값
k = Counter(arr).most_common()
if len(arr) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else: print(k[0][0])
else: print(arr[0])
# 범위
print((arr[-1] - arr[0]))