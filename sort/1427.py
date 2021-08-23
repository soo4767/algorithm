# https://www.acmicpc.net/problem/1427

n = input()

numbers = []

for i in n:
    numbers.append(i)
numbers.sort(reverse=True)

for i in numbers:
    print(i, end="")
