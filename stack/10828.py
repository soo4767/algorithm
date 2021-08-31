# https://www.acmicpc.net/problem/10828
import sys

stack = []

n = int(input())

for i in range(n):
    inp = list(sys.stdin.readline().split())
    cmd = inp[0]
    if cmd == "push":
        stack.append(int(inp[1]))
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
