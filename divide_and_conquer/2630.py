# https://www.acmicpc.net/problem/2630


white = 0
blue = 0


def div(paper):
    if check(paper) or len(paper) <= 1:
        return
    else:
        l = len(paper)
        # y,x
        tem = []
        for i in paper[: l // 2]:
            tem.append(i[: l // 2])
        div(tem)  # 1
        tem = []
        for i in paper[: l // 2]:
            tem.append(i[l // 2 :])
        div(tem)  # 1

        tem = []
        for i in paper[l // 2 :]:
            tem.append(i[: l // 2])
        div(tem)  # 1

        tem = []
        for i in paper[l // 2 :]:
            tem.append(i[l // 2 :])
        div(tem)  # 1


def check(paper):
    global blue, white
    ck = False
    for y in range(len(paper)):
        if 0 in paper[y] and 1 in paper[y]:
            return False
        else:
            if 1 in paper[y]:
                blue += 1
                return True
            else:
                white += 1
                return True


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

div(paper)

print(white)
print(blue)
