# https://www.acmicpc.net/problem/11651

n = int(input())

xy = []

for _ in range(n):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x: (x[1], x[0]))
for i in xy:
    print(i[0], i[1], sep=" ")
