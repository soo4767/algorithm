# https://www.acmicpc.net/problem/1018


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))

starts = ["W", "B"]
min = 1000

for i in range(n - 7):
    for j in range(m - 7):
        for s in starts:
            count = 0
            for y in range(i, i + 8):
                if y % 2 != 0:
                    if s == "W":
                        start = "B"
                    else:
                        start = "W"
                else:
                    start = s
                for x in range(j, j + 8):
                    if board[y][x] != start:
                        count += 1
                    if start == "W":
                        start = "B"
                    else:
                        start = "W"
            if count < min:
                min = count
print(min)
