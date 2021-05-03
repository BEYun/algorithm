n, m = map(int, input().split(' '))
check = [False] * (n+1)
arr = [0] * m

def dfs(index, n, m):
    if index == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if check[i] == True:
            continue
        arr[index] = i
        check[i] = True
        for j in range(i+1):
            check[j] = True
        dfs(index + 1, n, m)
        for k in range(1, n+1):
            check[k] = False

dfs(0, n, m)