def solution(elements):
    e = elements * 2
    r = set()
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            r.add(sum(e[j:j+i]))
    
    return len(r)
