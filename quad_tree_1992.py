import sys
N = int(sys.stdin.readline())
tree_array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def quad_tree(x, y, n):
    chk_cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tree_array[i][j]:
                chk_cnt += 1
            
    if not chk_cnt:
        print('0', end='')
    elif chk_cnt == n ** 2:
        print('1', end='')
    else:
        print('(', end='')
        quad_tree(x, y, n//2)
        quad_tree(x, y + n//2, n//2)
        quad_tree(x + n//2, y, n//2)
        quad_tree(x + n//2, y + n//2, n//2)
        print(')', end='')
    return

quad_tree(0, 0, N)
