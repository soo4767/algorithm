# https://www.acmicpc.net/problem/2740


N, M = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(N)]

M, K = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(M)]

# num[0][0] =  a[0][0] * b[0][0] + a[0][1]*b[1][0]
# num[0][1] =  a[0][0] * b[0][1] + a[0][1]*b[1][1]
# num[0][2] =  a[0][0] * b[0][2] + a[0][1]*b[1][2]

# num[2][0] =  a[1][0] * b[0][0] + a[1][1]*b[1][0]
# num[2][1] =  a[1][0] * b[0][1] + a[1][1]*b[1][1]
# num[2][2] =  a[1][0] * b[0][2] + a[1][1]*b[1][2]

# num[2][0] =  a[2][0] * b[0][0] + a[2][1]*b[1][0]
# num[2][1] =  a[2][0] * b[0][1] + a[2][1]*b[1][1]
# num[2][2] =  a[2][0] * b[0][2] + a[2][1]*b[1][2]

result = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += a[n][m] * b[m][k]

for row in result:
    for num in row:
        print(num, end=" ")
    print()
