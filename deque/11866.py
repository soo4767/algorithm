# https://www.acmicpc.net/problem/11866

n, k = list(map(int, input().split()))

# 1 2 3 4 ... n
li = [i for i in range(1, n + 1)]

arr = []

idx = k - 1
while len(arr) != n:
    if idx >= len(li):
        idx -= len(li)
        continue
    arr.append(li.pop(idx))
    idx += k - 1

print("<", end="")
for i in range(len(arr)):
    if i != len(arr) - 1:
        print(f"{arr[i]}, ", end="")
    else:
        print(f"{arr[i]}>", end="")
