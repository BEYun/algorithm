def fib(n):
    fib_arr = [[0, 0] for i in range(n+1)]
    fib_arr[0] = [1, 0]
    fib_arr[1] = [0, 1]
    if n == 0:
        return fib_arr[0]
    elif n == 1:
        return fib_arr[1]
    else:
        for i in range(2, n+1):
            if fib_arr[i] != [0, 0]:
                continue
            else:
                fib_arr[i][0] = fib_arr[i-2][0] + fib_arr[i-1][0]
                fib_arr[i][1] = fib_arr[i-2][1] + fib_arr[i-1][1]
    return fib_arr

T = int(input())
fib_arr = fib(40)
for _ in range(T):
    n = int(input())
    k = fib_arr[n]
    for i in k:
        print(i, end=" ")