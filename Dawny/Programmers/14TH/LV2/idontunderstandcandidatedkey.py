from itertools import combinations
def solution(relation):
    n = len(relation)
    m = len(relation[0])
    case = []
    for i in range(1, m+1):
        case += list(combinations(range(m), i))
        
    # 유일성
    key = []
    for j in case:
        tmp = [tuple(item[key] for key in j) for item in relation]
        if len(set(tmp)) == n:
            key.append(j)
    
    privatekey = set(key)

    # 최소성
    for i in range(len(key)):
        for j in range(i+1, len(key)):
            if len(key[i]) == len(set(key[i]).intersection(set(key[j]))):
                privatekey.discard(key[j])
    
    return len(privatekey)
