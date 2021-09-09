def solution(weights, head2head):
    # 승률 , 몸무게 무거운 복서 이긴횟수 , 몸무게 , idx
    answer = []
    result = []
    for vs in range(len(head2head)):
        vs_count = len(head2head[vs]) - head2head[vs].count("N")
        rate = 0
        if vs_count != 0:
            rate = head2head[vs].count("W") / vs_count
        weight = weights[vs]
        count = 0
        for w in weights:
            if weight < w:
                count += 1
        result.append([rate, count, weight, vs + 1])

    result.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    for r in result:
        answer.append(r[3])
    print(result)
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
