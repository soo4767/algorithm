# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.insert(0, int(input()))

count = 0
for coin in coins:
    count += k // coin
    k %= coin
print(count)
