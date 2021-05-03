import sys
timer = [300, 60, 10]
T = int(sys.stdin.readline())
time_cnt = [0, 0, 0]

for i in range(3):
    time_cnt[i] = T // timer[i]
    T = T % timer[i]

if T != 0:
    print('-1')
else:
    print(' '.join(str(time_cnt[i]) for i in range(3)))