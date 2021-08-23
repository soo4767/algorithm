# https://www.acmicpc.net/problem/10989
import sys

n = int(sys.stdin.readline())

numbers = [0 for _ in range(10001)]

for _ in range(n):
    numbers[int(sys.stdin.readline()) - 1] += 1

for i in range(len(numbers)):
    for j in range(numbers[i]):
        sys.stdout.write(str(i + 1) + "\n")
