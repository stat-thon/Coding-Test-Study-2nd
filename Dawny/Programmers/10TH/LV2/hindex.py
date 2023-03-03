from collections import Counter, deque

def solution(citations):
    s = len(citations)
    item = deque(sorted(Counter(citations).items()))
    if max(citations) == 0:
        return 0
    
    for i in range(1, max(citations)+2):
        while item and i > item[0][0]:
            a, b = item.popleft()
            s -= b
        if i >= s:
            break
    return i if i == s else i-1
