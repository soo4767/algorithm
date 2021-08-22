# https://www.acmicpc.net/problem/1436

n = int(input())
num_count = 0
numbers = []
i = 666
while True:
    string = str(i)
    count = 0
    for s in range(len(string) - 2):
        if string[s : s + 3] == "666":
            numbers.append(i)
            num_count += 1
            break
    if n == num_count:
        break
    i += 1

print(numbers[-1])
