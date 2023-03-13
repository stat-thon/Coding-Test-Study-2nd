from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    order = sorted(counter, key = lambda x: counter[x])
    cnt = 1
    while k:
        k -= 1
        if counter[order[-1]] > 0:
            counter[order[-1]] -= 1
        else:
            order.pop()
            cnt += 1
            counter[order[-1]] -= 1
    
    return cnt