# https://www.acmicpc.net/problem/14888

min2 = 987654321
max2 = -987654321
operaters = ["+", "-", "x", "//"]


def cal(operaters_num, numbers, operater):
    global min2
    global max2
    next_operaters_num = operaters_num[:]
    if len(numbers) == 1:
        if max2 < numbers[0]:
            max2 = numbers[0]
        if min2 > numbers[0]:
            min2 = numbers[0]
        return
    if next_operaters_num[operaters.index(operater)] == 0:
        return
    next_operaters_num[operaters.index(operater)] -= 1

    next_num = numbers[:]
    result = 0

    if operater == "+":
        result = next_num[0] + next_num[1]
    elif operater == "-":
        result = next_num[0] - next_num[1]
    elif operater == "x":
        result = next_num[0] * next_num[1]
    elif operater == "//":
        if next_num[0] < 0:
            result = -(abs(next_num[0]) // next_num[1])
        else:
            result = next_num[0] // next_num[1]

    del next_num[0]
    del next_num[0]

    next_num.insert(0, result)
    for i in range(len(next_operaters_num)):
        cal(next_operaters_num, next_num, operaters[i])


n = int(input())
numbers = list(map(int, input().split()))
operaters_num = list(map(int, input().split()))


for i in range(len(operaters_num)):
    cal(operaters_num, numbers, operaters[i])

print(max2)
print(min2)
