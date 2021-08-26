# https://www.acmicpc.net/problem/2580

board = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    board.append(list(map(int, input().split())))


while True:
    count_zero = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                continue
            count_zero += 1
            x_list = []
            y_list = []
            s_list = []

            for x in range(9):
                x_list.append(board[i][x])
            for y in range(9):
                y_list.append(board[y][j])
            i_start = (i // 3) * 3
            j_start = (j // 3) * 3
            for y in range(i_start, i_start + 3):
                for x in range(j_start, j_start + 3):
                    s_list.append(board[y][x])
            if x_list.count(0) == 1:
                remain = set(numbers) - set(x_list)
                board[i][j] = remain.pop()
                continue
            if y_list.count(0) == 1:
                remain = set(numbers) - set(y_list)
                board[i][j] = remain.pop()
                continue
            if s_list.count(0) == 1:
                remain = set(numbers) - set(s_list)
                board[i][j] = remain.pop()
                continue
    if count_zero == 0:
        break

for i in range(9):
    for j in range(9):
        print(board[i][j], end=" ")
        if j == 8:
            print("")
