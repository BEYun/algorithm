n = int(input())
x = 0
for i in range(1, n+1):
    i_list = list(map(int, str(i)))
    k = i + sum(i_list)
    if k == n:
        x = i
        break
print(x)
