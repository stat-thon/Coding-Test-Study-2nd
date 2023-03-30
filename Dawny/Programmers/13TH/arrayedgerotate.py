from collections import deque
def solution(rows, columns, queries):
    d = []
    
    arr = [[i+(j*columns) for i in range(1, columns+1)] for j in range(rows)]
    
    def curve(n1, m1, n2, m2):
        minnum = 100000
        point = deque([])
        for k in range(m1-1, m2):
            point.appendleft([n1-1, k])
            minnum = min(minnum, arr[n1-1][k])
        for k in range(n1, n2):
            point.appendleft([k, m2-1])
            minnum = min(minnum, arr[k][m2-1])
        for k in range(m2-2, m1-2, -1):
            point.appendleft([n2-1, k])
            minnum = min(minnum, arr[n2-1][k])
        for k in range(n2-2, n1-2, -1):
            point.appendleft([k, m1-1])
            minnum = min(minnum, arr[k][m1-1])
        x, y = point.popleft()
        tmp = arr[x][y]
        while point:
            a, b = point.popleft()
            arr[x][y] = arr[a][b]
            x, y = a, b
        arr[n1-1][m1] = tmp
        return minnum
    
    q = deque(queries)
    while q:
        n1, m1, n2, m2 = q.popleft()
        d.append(curve(n1, m1, n2, m2))

    return d
