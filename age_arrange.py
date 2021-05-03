n = int(input())
info_list = []

for i in range(n):
    info = list(map(str, input().split()))
    age = info[0]
    name = info[1]
    info_list.append((int(age), name, i))

info_list.sort(key=lambda x:(x[0], x[2]))

for i in range(n):
    print(info_list[i][0], info_list[i][1])