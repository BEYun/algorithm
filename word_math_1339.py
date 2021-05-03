import sys
input = sys.stdin.readline

N = int(input())
words = []
result = 0
for _ in range(N):
    words.append(list(map(str, input().rstrip())))

words_num = {}
for word in words:
    cnt = 1
    for i in range(len(word)-1, -1, -1):
        if word[i] not in words_num.keys():
            words_num[word[i]] = cnt
        else:
            words_num[word[i]] += cnt
        cnt *= 10

words_num = list(sorted(words_num.items(), key=lambda x:x[1], reverse=True))
k = 9
for num in words_num:
    result += num[1] * k
    k -= 1
print(result)
