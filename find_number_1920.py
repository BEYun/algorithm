import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
n_arr = sorted(list(map(int, input().split())))
M = int(input())
m_arr = list(map(int, input().split()))

result = {}
for n in n_arr:
    if n not in result:
        result[n] = 1

for m in m_arr:
    if m in result:
        print('1')
    else:
        print('0')