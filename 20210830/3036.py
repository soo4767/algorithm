# https://www.acmicpc.net/problem/3036

n = int(input())
numbers = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(1, n):
    g = gcd(numbers[0], numbers[i])
    print(f"{numbers[0]//g}/{numbers[i]//g}")
