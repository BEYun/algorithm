import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
n_cards = sorted(list(map(int, input().split())))

M = int(input())
m_cards = list(map(int, input().split()))
result = {}
index = 0

# 첫번째 방법(N, M 정렬 후 인덱스로 count)
# for m in sorted(m_cards):
#     cnt = 0
#     if m not in result:
#         while index <= N-1:
#             if m == n_cards[index]:
#                 index += 1
#                 cnt += 1
#             elif m > n_cards[index]:
#                 index += 1
#             else:
#                 break
#         result[m] = cnt
# print(' '.join(str(result[m]) for m in m_cards))

# 두번째 방법(hash 이용)
# for n in n_cards:
#     if n in result:
#         result[n] += 1
#     else:
#         result[n] = 1
#print(' '.join(str(result[m]) if m in result else '0' for m in m_cards))

# 세번째 방법(counter 이용)
c = Counter(n_cards)
print(' '.join(str(c[m]) for m in m_cards))