# https://www.acmicpc.net/problem/1932
# sum2 = []
# n = int(input())
# li = []
# for _ in range(n):
#     li.append(list(map(int, input().split())))


# def li_sum(start, sum):
#     if start[0] == len(li) - 1:
#         sum2.append(sum + li[start[0]][start[1]])
#         return
#     try:
#         li_sum((start[0] + 1, start[1] + 1), sum + li[start[0]][start[1]])
#     except:
#         pass
#     li_sum((start[0] + 1, start[1]), sum + li[start[0]][start[1]])


# tr_sum((0, 0), 0)
# print(max(sum2))


n = int(input())
tr = []


for _ in range(n):
    tr.append(list(map(int, input().split())))


for layer in range(1, n):
    l = len(tr[layer])
    for i in range(l):
        temp = []
        if 0 <= i - 1:
            temp.append(tr[layer - 1][i - 1])
        if i < l - 1:
            temp.append(tr[layer - 1][i])
        tr[layer][i] += max(temp)
        for kx in tr:
            print(kx)
print(max(tr[n - 1]))
