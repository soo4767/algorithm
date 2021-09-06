# https://www.acmicpc.net/problem/2839

# 3kg 5kg

n = int(input())
cnt = 0
while True:
    if (n - 3 * cnt) % 5 == 0:
        print((n - 3 * cnt) // 5 + cnt)
        break
    elif n - 3 * cnt == 0:
        print(n // 3)
        break
    elif n - 3 * cnt < 0:
        print(-1)
        break
    cnt += 1
