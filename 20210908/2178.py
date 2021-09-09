# https://www.acmicpc.net/problem/2178

from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                que.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1

    for i in graph:
        print(i)
    return graph[n - 1][m - 1]


n, m = list(map(int, input().split()))
graph = [list(map(int, input())) for _ in range(n)]

x = 0
y = 0
# 상하좌우
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

print(bfs(x, y))
