# https://www.acmicpc.net/problem/10773

n = int(input())

money = []

for i in range(n):
    number = int(input())
    if number == 0:
        money.pop()
    else:
        money.append(number)

print(sum(money))
