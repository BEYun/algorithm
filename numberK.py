def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        result = array[commands[i][0]-1:commands[i][1]]
        result.sort()
        cnt = commands[i][2] - 1
        answer.append(result[cnt])
    
    return answer
    
