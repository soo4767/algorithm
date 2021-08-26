# https://www.acmicpc.net/problem/11054

n = int(input())

numbers = list(map(int, input().split()))

increase = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            increase[i] = max(increase[i], increase[j] + 1)

decrease2 = [1 for i in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if numbers[i] > numbers[j]:
            decrease2[i] = max(decrease2[i], decrease2[j] + 1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease2[i] - 1

print(max(result))
