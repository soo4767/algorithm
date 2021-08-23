# https://www.acmicpc.net/problem/1181

n = int(input())

words = []

for _ in range(n):
    words.append(input())
clean_words = list(set(words))
clean_words.sort(key=lambda x: (len(x), x))
for i in clean_words:
    print(i)
