n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
start_select = [0 for i in range(n)]

min_stat = 2001

def dfs(idx, cnt):
    global min_stat
    if cnt == n / 2:
        start_stat = 0
        link_stat = 0
        for i in range(n):
            for j in range(n):
                if start_select[i] == 1 and start_select[j] == 1:
                    start_stat += s[i][j]
                elif start_select[i] == 0 and start_select[j] == 0:
                    link_stat += s[i][j]
        min_stat = min(min_stat, abs(start_stat-link_stat))
        return
    
    for i in range(idx, n):
        if start_select[i] == 1:
            continue
        start_select[i] = 1
        dfs(i+1, cnt+1)
        start_select[i] = 0
        
dfs(0, 0)
print(min_stat)