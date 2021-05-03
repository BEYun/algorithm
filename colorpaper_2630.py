import sys

N = int(sys.stdin.readline())
paper_array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
w_cnt, b_cnt = 0, 0

def div_conq(x, y, n):
    global w_cnt, b_cnt
    cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper_array[i][j]:
                cnt += 1
    
    if not cnt:
        w_cnt += 1
    elif cnt == n**2:
        b_cnt += 1
    else:
        div_conq(x, y, n//2)
        div_conq(x + n//2, y, n//2)
        div_conq(x, y + n//2, n//2)
        div_conq(x + n//2, y + n//2, n//2)
    return

div_conq(0, 0, N)
print(w_cnt)
print(b_cnt)