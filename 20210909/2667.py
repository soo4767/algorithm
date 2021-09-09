# https://www.acmicpc.net/problem/2667
def dfs(x, y):
    count = 0
    if x < 0 or y < 0 or x >= n or y >= n:
        return count
    if graph[y][x] != 1:
        return count
    count += 1
    graph[y][x] = 2
    for i in range(4):
        count += dfs(x + dx[i], y + dy[i])
    return count


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

house=[]

for y in range(len(graph)):
    for x in range(len(graph[0])):
        c = dfs(x, y)
        if c != 0 :
            house.append(c)

house.sort()

print(len(house))

for i in house:
    print(i)