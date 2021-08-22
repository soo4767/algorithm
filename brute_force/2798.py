# https://www.acmicpc.net/problem/2798
# n장의 카드에서 3장 M과 최대한 가깝게
n, m = map(int, input().split())
cards = list(map(int, input().split()))

min = 987654321
result = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum > m:
                continue
            if m - sum < min:
                min = m - sum
                result = sum
print(result)
