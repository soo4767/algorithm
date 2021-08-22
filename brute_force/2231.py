# https://www.acmicpc.net/problem/2231

n = int(input())
result = 0
for i in range(n):
    s = str(i)
    sum = i
    for j in s:
        sum += int(j)
    if sum == n:
        result = i
        break
print(result)
