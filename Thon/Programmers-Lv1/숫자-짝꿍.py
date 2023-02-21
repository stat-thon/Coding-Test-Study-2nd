from collections import Counter
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    
    result = ''
    for s in '9876543210':
        if s in X.keys() and s in Y.keys():
            result += s * min(X[s], Y[s])
    
    if result == '':
        result = '-1'
    
    while result.startswith('0'):
        result = result[1:]
        if len(result) == 1:
            break
    return result