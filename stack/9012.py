# https://www.acmicpc.net/problem/9012

n = int(input())

for i in range(n):
    ps = list(input())
    vps = []
    for j in ps:
        if j == "(":
            vps.append(j)
        else:
            if "(" in vps:
                vps.pop()
            else:
                vps.append(")")
                
    if len(vps) == 0 :
        print("YES")
    else:
        print("NO")
