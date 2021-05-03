line = input().split('-')
num = []

for i in line:
    i = i.split('+')
    tmp = 0
    for j in i:
        tmp += int(j)
    num.append(tmp)

answer = num[0]
for k in range(1, len(num)):
    answer -= num[k]

print(answer)
