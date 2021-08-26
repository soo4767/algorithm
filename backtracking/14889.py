# https://www.acmicpc.net/problem/14889
from itertools import combinations

min = 987654321
s = []
n = int(input())
people = [i for i in range(n)]
for i in range(n):
    j = list(map(int, input().split()))
    s.append(j)
for a_team in combinations(people, len(people) // 2):
    a_sum = 0
    b_sum = 0
    b_tema = list(set(people) - set(a_team))
    for point in combinations(a_team, 2):
        a_sum = a_sum + s[point[0]][point[1]] + s[point[1]][point[0]]
    for point in combinations(b_tema, 2):
        b_sum = b_sum + s[point[0]][point[1]] + s[point[1]][point[0]]
    if abs(a_sum - b_sum) < min:
        min = abs(a_sum - b_sum)

print(min)
