n, m = map(int, input().split(' '))
arr = [0 for i in range(m)]

def dfs(index, n, m):
    if index == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        arr[index] = i
        dfs(index + 1, n, m)

dfs(0, n, m)