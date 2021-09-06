# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    que = deque()
    que.append(v)
    visited[v] = True

    while que:
        a = que.popleft()
        print(a, end=" ")
        for i in graph[a]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

print(graph)
dfs(graph, v, visited)

print()
visited2 = [False] * (n + 1)

bfs(graph, v, visited2)
