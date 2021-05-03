n, m = map(int, input().split(' '))
arr = [0 for i in range(m)]

def dfs(index, next):
    if index == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(next, n+1):
        arr[index] = i
        dfs(index + 1, i)

dfs(0, 1)