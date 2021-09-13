# https://www.acmicpc.net/problem/2606


def vfs(number):
    if visit[number] == 1:
        return
    visit[number] = 1
    for i in graph[number]:
        vfs(i)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

vfs(1)
print(sum(visit) - 1)
