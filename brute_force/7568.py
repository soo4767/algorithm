# https://www.acmicpc.net/problem/7568

n = int(input())
people = []
for _ in range(n):
    s_info = list(map(int, input().split()))
    people.append(s_info)

for i in range(n):
    target = people[i]
    bigger = 0
    for j in range(n):
        if target[0] < people[j][0] and target[1] < people[j][1]:
            bigger += 1
    people[i].append(bigger)


for i in range(n):
    print(people[i][2] + 1, end=" ")
