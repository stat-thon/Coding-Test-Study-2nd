def solution(k, m, score):
    score.sort()
    a = 0
    while len(score) >= m:
        a += min(score[-m:])*m
        for _ in range(m):
            score.pop()
    return a
