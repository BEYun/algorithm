n = int(input())
a = list(map(int, input().split(' ')))
p, m, mul, div = map(int, input().split(' '))
op_max = -1000000001
op_min = 1000000001
k = 0

def dfs(cnt, result, p, m, mul, div):
    global op_max
    global op_min
    global k
    if cnt == n:
        op_max = max(op_max, result)
        op_min = min(op_min, result)
        k += 1
        print('k=',k)
        print('result=',result)
        return
    if p:
        dfs(cnt+1, result+a[cnt], p-1, m, mul, div)
    if m:
        dfs(cnt+1, result-a[cnt], p, m-1, mul, div)
    if mul:
        dfs(cnt+1, result*a[cnt], p, m, mul-1, div)
    if div:
        dfs(cnt+1, -(-result // a[cnt]) if result < 0 else result // a[cnt], p, m, mul, div-1)

dfs(1, a[0], p, m, mul, div)
print(op_max)
print(op_min)