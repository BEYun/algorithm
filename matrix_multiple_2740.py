import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = [[0 for _ in range(K)] for _ in range(N)]

def matrix_mul(a, b):
    for n in range(N):
        for k in range(K):
            for m in range(M):
                result[n][k] += a[n][m] * b[m][k]        

matrix_mul(A, B)

for i in result:
    for j in i:
        print(j, end=' ')
    print()