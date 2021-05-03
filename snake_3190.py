from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_arr = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    n_arr[a-1][b-1] = 1

l = int(input())
rot_times = {}
for _ in range(l):
    s, c = map(str, input().split())
    rot_times[int(s)] = c

def rot(rotation, c):
    if c == 'L':
        rotation = (rotation - 1) % 4
    else:
        rotation = (rotation + 1) % 4
    return rotation

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

rotation = 1
snake = deque([[0,0]])
x, y = 0, 0
n_arr[x][y] = 2
time = 1

while True:
    x += dx[rotation-1]
    y += dy[rotation-1]
    if 0 <= x < n and 0 <= y < n and n_arr[x][y] != 2:    
        if n_arr[x][y] != 1:
            tmp_x, tmp_y = snake.pop()
            n_arr[tmp_x][tmp_y] = 0
        n_arr[x][y] = 2
        snake.appendleft([x, y])
        if time in rot_times.keys():
            rotation = rot(rotation, rot_times[time])
        time += 1
    else:
        break

print(time)
