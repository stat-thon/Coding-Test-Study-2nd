from collections import Counter

def solution(weights):
    result = 0
    wdict = Counter(weights)
    weight = [2/3, 2/4, 3/4]
    for key in wdict.keys():
        if wdict[key] > 1:
            result += (wdict[key] * (wdict[key] - 1)) / 2
        
        for w in weight:
            nw = key * w
            if nw in wdict.keys():
                result += wdict[key] * wdict[nw]
    
    return result