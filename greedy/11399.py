# https://www.acmicpc.net/problem/11399

n = int(input())

people = list(map(int, input().split()))

people.sort()
a_sum = 0
for i in range(n):
    p_sum = 0
    for j in range(i + 1):
        p_sum += people[j]
    a_sum += p_sum
print(a_sum)
