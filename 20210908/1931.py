# https://www.acmicpc.net/problem/1931

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: (x[1], x[0]))

d = []
d.append(li[0])

for i in range(1, len(li)):
    if d[-1][1] <= li[i][0]:  # 끝나는 시간이 시작시간보다 작으면
        d.append(li[i])

print(len(d))
