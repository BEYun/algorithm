n, m = map(int, input().split(' '))
check = [False for i in range(n+1)]
arr = [0 for i in  range(m)]

def dfs(index, n, m):
    if index == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
        
    for i in range(1, n+1):
        if check[i] == True:
            continue
        check[i] = True
        arr[index] = i
        dfs(index+1, n, m)
        check[i] = False


dfs(0, n, m)