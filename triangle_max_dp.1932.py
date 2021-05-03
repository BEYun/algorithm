import sys
n = int(sys.stdin.readline())
triangle = []
for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

tri_sum = [[0] * i for i in range(1, n+1)]

for i in range(n):
    for j in range(len(triangle[i])):
        if i == 0:
            tri_sum[i][j] = triangle[i][j]
        if j == 0:
            tri_sum[i][j] = tri_sum[i-1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            tri_sum[i][j] = tri_sum[i-1][j-1] + triangle[i][j]
        else:
            tri_sum[i][j] = max(tri_sum[i-1][j-1], tri_sum[i-1][j]) + triangle[i][j]

print(max(tri_sum[-1]))