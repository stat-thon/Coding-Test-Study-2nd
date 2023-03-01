from collections import Counter as cnt
def solution(k, tangerine):
    a = 0
    b = 0
    for i, j in sorted(list(cnt(tangerine).items()), key = lambda x: -x[1]):
        b += j
        a += 1
        if b >= k:
            return a
