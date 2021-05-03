import sys

T = int(sys.stdin.readline())

for _ in range(T):
    com = list(map(str, sys.stdin.readline().strip()))
    N = int(sys.stdin.readline())
    N_list = sys.stdin.readline().rstrip()[1:-1].split(',')
    is_reverse = False

    while com:
        if com[0] == 'R':
            is_reverse = not is_reverse
            com.pop(0)
        
        elif com[0] == "D":
            if not N_list or N_list[0] == '':
                print('error')
                break
            else:
                if is_reverse == True:
                    N_list.pop()
                    com.pop(0)

                else:
                    N_list.pop(0)
                    com.pop(0)
        if not com:
            if is_reverse == True:
                print('['+','.join(N_list[::-1])+']')
            else:
                print('['+','.join(N_list)+']')