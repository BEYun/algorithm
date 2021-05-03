from itertools import combinations
import sys
dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))
arr = list(combinations(dwarf, 7))
for k in arr:
    if sum(k) == 100:
        k = sorted(k)
        for i in k:
            print(i)
        break