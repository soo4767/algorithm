# https://www.acmicpc.net/problem/1463
from collections import deque

que = deque()
n = int(input())
count = 0
dp = [False] * (n + 1)
que.append([n, 0])
while count == 0:
    num, num_count = que.popleft()
    if dp[num]:
        continue
    dp[num] = True
    if num == 1:
        count = num_count
        break
    if num % 3 == 0:
        que.append([num // 3, num_count + 1])
    if num % 2 == 0:
        que.append([num // 2, num_count + 1])
    que.append([num - 1, num_count + 1])

print(count)
