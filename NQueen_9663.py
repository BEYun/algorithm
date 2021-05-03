n = int(input())
chess = [0 for i in range(n)]
answer = 0

def isTrue(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i:
            return False
    return True

def n_queen(cnt):
    global answer
    if cnt == n:
        answer += 1
    else:
        for i in range(n):
            chess[cnt] = i
            if isTrue(cnt):
                n_queen(cnt+1)

n_queen(0)
print(answer)

