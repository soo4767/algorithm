# https://www.acmicpc.net/problem/11050


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


n, k = map(int, input().split())

print(factorial(n) // (factorial(n - k) * factorial(k)))
