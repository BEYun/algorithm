T = int(input())
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for _ in range(T):
    n = int(input())
    if d[n] != 0:
        print(d[n])
    else:
        for i in range(4, n+1):
            if d[i] != 0:
                continue
            else:
                d[i] = d[i-3] + d[i-2]
        print(d[n])