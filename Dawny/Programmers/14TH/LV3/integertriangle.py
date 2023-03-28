def solution(triangle):
    t = list(map(lambda x: [0]+x+[0], triangle))
    n = len(t)
    for i in range(1, n):
        for j in range(1, i+2):
            t[i][j] += max(t[i-1][j], t[i-1][j-1])
        
    return max(t[-1])
