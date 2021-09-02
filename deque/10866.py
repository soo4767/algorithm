from collections import deque
import sys

que = deque()

n = int(input())

for i in range(n):
    inp = list(sys.stdin.readline().split())
    cmd = inp[0]

    if cmd == "push_front":
        que.appendleft(inp[1])
    elif cmd == "push_back":
        que.append(inp[1])
    elif cmd == "pop_front":
        if len(list(que)) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(list(que)) != 0:
            print(que.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(list(que)))
    elif cmd == "empty":
        if len(list(que)) != 0:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if len(list(que)) != 0:
            print(list(que)[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(list(que)) != 0:
            print(list(que)[-1])
        else:
            print(-1)
