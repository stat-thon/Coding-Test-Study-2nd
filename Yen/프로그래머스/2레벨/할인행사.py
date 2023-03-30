def solution(want, number, discount):
    answer, wants = 0, []
    for v, n in zip(want, number):
        wants += [v]*n
    wants = sorted(wants)
    for i, product in enumerate(discount[:-len(wants)+1]):
        if product in wants:
            if wants == sorted(discount[i:len(wants)+i]):
                answer += 1

    return answer
