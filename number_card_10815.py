import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

# check_dict = {}
# for c in cards:
#     check_dict[c] = 1

# for c in check:
#     if c in check_dict.keys():
#         print('1', end=' ')
#     else:
#         print('0', end=' ')

check_dict = Counter(cards)
print(' '.join('1' if k in check_dict.keys() else '0' for k in check))