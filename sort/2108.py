# https://www.acmicpc.net/problem/2108
n = int(input())

numbers = []
b = {}
for _ in range(n):
    num = int(input())
    numbers.append(num)
    if b.get(num) is None:
        b[num] = 0
    else:
        b[num] += 1
numbers.sort()

max_list = []
max = 0

keys = b.keys()
for i in keys:
    if b[i] == max:
        max_list.append(i)
    elif b[i] > max:
        max_list.clear()
        max_list.append(i)
        max = b[i]
max_list.sort()
print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])
print(numbers[-1] - numbers[0])
